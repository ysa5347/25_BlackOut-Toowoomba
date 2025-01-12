import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import pickle

# in local
def generate_sample_data_50():
    np.random.seed(42)
    
    # 50개의 등간격 포인트 생성
    t = np.linspace(0, 4 * np.pi, 50)
    x = t
    y = np.sin(t)
    
    # 무작위로 10개의 인덱스 선택하여 이상치 생성
    outlier_indices = np.random.choice(50, 10, replace=False)
    
    # 선택된 포인트들을 sin 그래프에서 약간 벗어나게 조정
    y[outlier_indices] += np.random.uniform(0.5, 1.0, 10) * np.random.choice([-0.2, 0.2], 10)
    
    data = pd.DataFrame({'x': x, 'y': y})
    return data

def detect_outliers_with_dbscan_50(data, eps=0.3, min_samples=3):
    coordinates = data[['x', 'y']].values
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    data['cluster'] = dbscan.fit_predict(coordinates)

    # 모델 저장
    with open('dbscan_model.pkl', 'wb') as f:
        pickle.dump(dbscan, f)
    return data

def count_outliers(data):
    # cluster가 -1이 아닌 데이터 포인트가 이상치입니다
    outliers_count = len(data[data['cluster'] != -1])
    return outliers_count

def plot_routes_2d_50(data):
    plt.figure(figsize=(12, 8))
    
    # 기준이 되는 sin 곡선 그리기
    t = np.linspace(0, 4 * np.pi, 200)
    plt.plot(t, np.sin(t), 'b--', alpha=0.3, label='Reference sin curve')
    
    normal_data = data[data['cluster'] == -1]
    outliers = data[data['cluster'] != -1]
    
    plt.scatter(normal_data['x'], normal_data['y'], c=normal_data['cluster'], 
               cmap='viridis', label="Normal Data", s=100, alpha=0.7)
    plt.scatter(outliers['x'], outliers['y'], c='red', label="Outliers", 
               s=100, alpha=0.9)
    
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("50 Points on Sin Curve with Outliers")
    plt.legend()
    plt.grid(True)
    
        # 분석 결과를 딕셔너리로 반환
    result = {
        'figure': plt.gcf(),  # 현재 그래프 figure 객체
        'normal_points': {
            'data': normal_data.to_dict('records'),
            'count': len(normal_data)
        },
        'outlier_points': {
            'data': outliers.to_dict('records'),
            'count': len(outliers)
        },
        'outlier_count': count_outliers(data)
    }
    return result

def score3(sample_data: list) -> list[int]:
    data = generate_sample_data_50()
    data_with_clusters = detect_outliers_with_dbscan_50(data)
    results = plot_routes_2d_50(data_with_clusters)
    weight = -0.1
    return results['outlier_count'] * weight

# 실행
#data_50 = generate_sample_data_50()
#data_50_with_clusters = detect_outliers_with_dbscan_50(data_50)
#plot_routes_2d_50(data_50_with_clusters)