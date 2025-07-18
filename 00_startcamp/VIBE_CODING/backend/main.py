# FastAPI 진입점
from fastapi import FastAPI

app = FastAPI()

# 기존 루트 엔드포인트
@app.get('/')
def read_root():
    return {"message": "Running Rhythm Sync API"}

# 심박수/케이던스 mock 데이터 엔드포인트
import random

@app.get('/mock-data')
def get_mock_data():
    hr = random.randint(100, 180)
    cadence = random.randint(150, 200)
    return {"current_hr": hr, "current_cadence": cadence}

# BPM 추천 엔드포인트
from fastapi import Query

@app.get('/recommend-bpm')
def recommend_bpm(current_hr: int = Query(...), current_cadence: int = Query(...), target_hr: int = Query(...), target_cadence: int = Query(...)):
    bpm = (current_hr + current_cadence) / 2
    if abs(bpm - target_hr) > 10:
        bpm = target_hr
    return {"recommended_bpm": int(bpm)}
