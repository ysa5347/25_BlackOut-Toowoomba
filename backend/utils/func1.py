# 선행 score api
#sample_data = pd.read_csv("sample_data.csv")

# roll 값이 70 이상이면 True(기울어짐)), 아니면 False
def is_fallen(sample_data: list) -> list[int]:
    critical_angle = 70
    return [1 if abs(roll) > critical_angle else 0 for roll in sample_data]

# 위의 roll 값 기준으로 점수 계산
def score1(sample_data: list) -> list[int]:
    weight = 10
    return list(map(lambda x: x * weight, is_fallen(sample_data)))


