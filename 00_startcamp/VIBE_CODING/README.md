# 러닝 리듬 동기화 앱 (프로토타입)

## 프로젝트 개요

사용자가 입력한 목표 심박수와 케이던스를 기준으로, 실시간으로 측정되는 현재 심박수/케이던스를 비교하여 가장 적합한 BPM(분당 박자 수)의 음악을 자동으로 재생하는 웹앱입니다. 음악은 Spotify API 또는 YouTube API를 통해 자동으로 전환됩니다.

---

## 기술 스택

- **프론트엔드**: Streamlit (파이썬 기반 웹 프레임워크)
- **백엔드**: FastAPI (RESTful API 서버)
- **음악 API**: Spotify Web API (우선 구현)

---

## 폴더 구조

```
VIBE_CODING/
│
├── backend/
│   ├── main.py                # FastAPI 진입점
│   ├── models.py              # 데이터 모델 정의
│   ├── api/
│   │   ├── endpoints.py       # REST API 엔드포인트
│   │   └── spotify.py         # Spotify API 연동 모듈
│   ├── services/
│   │   ├── bpm_matcher.py     # BPM-음악 매칭 알고리즘
│   │   └── mock_sensor.py     # 심박수/케이던스 mock 데이터 생성
│   └── requirements.txt       # 백엔드 의존성
│
├── frontend/
│   ├── app.py                 # Streamlit 앱 진입점
│   ├── components/
│   │   ├── input_form.py      # 사용자 입력 폼
│   │   └── music_player.py    # 음악 플레이어 UI
│   └── requirements.txt       # 프론트엔드 의존성
│
├── README.md                  # 프로젝트 설명서
└── .env                       # 환경 변수 (API 키 등)
```

---

## 개발 워크플로우

1. **초기 세팅**
   - 폴더 구조 생성 및 의존성 설치
   - `.env` 파일에 API 키/시크릿 등 환경 변수 저장

2. **백엔드 개발**
   - FastAPI로 RESTful API 서버 구축
   - 심박수/케이던스 mock 데이터 생성
   - BPM-음악 매칭 알고리즘 구현
   - Spotify API 연동 및 인증 처리

3. **프론트엔드 개발**
   - Streamlit으로 사용자 입력 폼 및 실시간 데이터 시각화 UI 구현
   - 음악 자동 재생 및 상태 변화에 따른 곡 전환 UI 구현
   - 백엔드 API와 통신

4. **통합 및 테스트**
   - 프론트엔드-백엔드 연동 테스트
   - 실시간 mock 데이터 기반 음악 자동 전환 테스트

---

## API 연동 및 인증 방식

### Spotify API 사용 예시

- **OAuth 2.0 인증**: Client Credentials Flow로 Access Token 획득
- **음악 검색 및 재생**: `/v1/search`, `/v1/me/player/play` 등 엔드포인트 활용

```python
# backend/api/spotify.py
import requests

def get_access_token(client_id, client_secret):
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={'grant_type': 'client_credentials'},
        auth=(client_id, client_secret)
    )
    return response.json()['access_token']

def search_tracks_by_bpm(access_token, bpm):
    headers = {'Authorization': f'Bearer {access_token}'}
    query = f'tempo:{bpm}'
    response = requests.get(
        f'https://api.spotify.com/v1/search?q={query}&type=track',
        headers=headers
    )
    return response.json()
```

---

## BPM과 음악 매칭 알고리즘

1. **입력값**: 목표 심박수, 목표 케이던스
2. **실시간 데이터**: 현재 심박수, 현재 케이던스 (mock)
3. **BPM 계산**:
   - 추천 BPM = (현재 케이던스 + 현재 심박수) / 2
4. **음악 매칭**:
   - Spotify에서 BPM(tempo) 메타데이터 기반으로 곡 검색
   - 추천 BPM과 가장 근접한 곡 자동 선택 및 재생

```python
# backend/services/bpm_matcher.py
def recommend_bpm(current_hr, current_cadence, target_hr, target_cadence):
    bpm = (current_hr + current_cadence) / 2
    if abs(bpm - target_hr) > 10:
        bpm = target_hr
    return int(bpm)
```

---

## 참고

- [Spotify for Developers](https://developer.spotify.com/documentation/web-api/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)

---

프로토타입 개발에 필요한 핵심 구조와 워크플로우를 정리했습니다. 추가 구현 예시나 코드가 필요하면 언제든 요청해 주세요.
