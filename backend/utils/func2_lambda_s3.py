import boto3
import base64
import json

# in aws lambda
def lambda_handler(event, context):
    s3_client = boto3.client('s3', region_name='us-east-1')
    lambda_client = boto3.client('lambda', region_name='us-east-1')

    # S3에서 파일 경로 가져오기
    bucket_name = event.get('bucket_name', 'blackout-27')
    object_key = event.get('object_key', 'good.jpg')

    try:
        # S3에서 이미지 가져오기
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        image_data = response['Body'].read()  # 바이너리 데이터 읽기

        # Base64로 인코딩
        base64_image = base64.b64encode(image_data).decode('utf-8')

        # Lambda 2 호출
        target_lambda_name = "bedrock-sonnect-image-classifier"  # Lambda 2 함수 이름
        response = lambda_client.invoke(
            FunctionName=target_lambda_name,
            InvocationType='RequestResponse',  # 동기 호출
            Payload=json.dumps({"base64_image": base64_image})
        )

        # Lambda 2 응답 읽기
        response_payload = json.load(response['Payload'])
        
        is_Positive = None
        positive_corpus = ['네', '예','맞습니다.']
        negative_corpus = ['아니요', '아닙니다.']
        if response_payload in positive_corpus:
            is_Positive = True
        elif response_payload in negative_corpus:
            is_Positive = False
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Api Results!",
                "response": response_payload,
                "is_Positive": is_Positive
            })
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def score2(sample_data: int) -> int:
    results = lambda_handler(sample_data)
    weight = 10
    return results['is_Positive'] * weight