# 심박수/케이던스 mock 데이터 생성 예시
import random

def get_mock_hr():
    return random.randint(100, 180)

def get_mock_cadence():
    return random.randint(150, 200)
