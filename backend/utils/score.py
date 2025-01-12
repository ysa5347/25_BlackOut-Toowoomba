import json
from utils.func1 import score1
from utils.func2_lambda_s3 import score2
from utils.func3_lambda_ml import score3

def score(sample_data: json) -> float:
    return score1(sample_data['roll']) + score2(sample_data) + score3(sample_data)