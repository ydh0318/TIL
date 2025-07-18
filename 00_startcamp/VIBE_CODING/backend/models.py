# 데이터 모델 정의 (예시)
class UserInput:
    def __init__(self, target_hr: int, target_cadence: int):
        self.target_hr = target_hr
        self.target_cadence = target_cadence
