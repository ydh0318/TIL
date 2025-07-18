# Streamlit 앱 진입점 예시
import streamlit as st
import requests
st.title('러닝 리듬 동기화 앱')
st.write('목표 심박수와 케이던스를 입력하세요.')


st.title('러닝 리듬 동기화 앱')

# 사용자 입력
st.subheader('목표 입력')
target_hr = st.number_input('목표 심박수', min_value=60, max_value=200, value=140)
target_cadence = st.number_input('목표 케이던스', min_value=100, max_value=220, value=170)

# mock 데이터 가져오기

# 목표 입력 후 추천 버튼
if st.button('추천 음악 보기'):
    # BPM 추천 API 호출 (목표값만 사용, 현재값은 목표값과 동일하게 전달)
    bpm_res = requests.get(
        'http://localhost:8000/recommend-bpm',
        params={
            'current_hr': target_hr,
            'current_cadence': target_cadence,
            'target_hr': target_hr,
            'target_cadence': target_cadence
        }
    )
    if bpm_res.status_code == 200:
        bpm_data = bpm_res.json()
        recommended_bpm = bpm_data['recommended_bpm']
        st.success(f"추천 BPM: {recommended_bpm}")

        # BPM 구간별 다양한 곡 리스트
        bpm_sections = [
            {
                "range": (90, 110),
                "tracks": [
                    {"name": "Ed Sheeran - Shape of You", "bpm": 96, "youtube_id": "JGwWNGJdvx8"},
                    {"name": "Charlie Puth - Attention", "bpm": 100, "youtube_id": "nfs8NYg7yQM"},
                    {"name": "Bruno Mars - Treasure", "bpm": 108, "youtube_id": "nPvuNsRccVw"},
                    {"name": "Red Velvet - Psycho", "bpm": 104, "youtube_id": "uR8Mrt1IpXg"}
                ]
            },
            {
                "range": (111, 125),
                "tracks": [
                    {"name": "BTS - Dynamite", "bpm": 114, "youtube_id": "gdZLi9oWNZg"},
                    {"name": "TWICE - Feel Special", "bpm": 120, "youtube_id": "3ymwOvzhwHs"},
                    {"name": "Lady Gaga - Poker Face", "bpm": 120, "youtube_id": "bESGLojNYSo"},
                    {"name": "Dua Lipa - Don't Start Now", "bpm": 124, "youtube_id": "oygrmJFKYZY"},
                    {"name": "ITZY - WANNABE", "bpm": 122, "youtube_id": "fE2h3lGlOsk"}
                ]
            },
            {
                "range": (126, 140),
                "tracks": [
                    {"name": "NewJeans - Super Shy", "bpm": 128, "youtube_id": "ArmDp-zijuc"},
                    {"name": "IVE - I AM", "bpm": 128, "youtube_id": "6ZUIwj3FgUY"},
                    {"name": "BLACKPINK - DDU-DU DDU-DU", "bpm": 140, "youtube_id": "IHNzOHi8sJs"},
                    {"name": "aespa - Spicy", "bpm": 132, "youtube_id": "Os_heh8vPfs"},
                    {"name": "LE SSERAFIM - UNFORGIVEN", "bpm": 132, "youtube_id": "UBURTQoe9lU"}
                ]
            },
            {
                "range": (141, 160),
                "tracks": [
                    {"name": "SEVENTEEN - HOT", "bpm": 148, "youtube_id": "VCDWg0ljbFQ"},
                    {"name": "Stray Kids - God's Menu", "bpm": 150, "youtube_id": "TQTlCHxyuu8"},
                    {"name": "NCT 127 - Cherry Bomb", "bpm": 150, "youtube_id": "w9uT7pM8b-k"},
                    {"name": "ITZY - Sneakers", "bpm": 152, "youtube_id": "Hbb5GPxXF1w"}
                ]
            },
            {
                "range": (161, 180),
                "tracks": [
                    {"name": "BLACKPINK - Boombayah", "bpm": 125, "youtube_id": "bwmSjveL3Lc"},
                    {"name": "BTS - Fire", "bpm": 170, "youtube_id": "0lapF4DQPKQ"},
                    {"name": "EXO - Power", "bpm": 174, "youtube_id": "KSH-FVVtTf0"},
                    {"name": "TWICE - Dance The Night Away", "bpm": 176, "youtube_id": "Fm5iP0S1z9w"}
                ]
            }
        ]

        # 추천 BPM이 속한 구간의 곡 리스트 선택
        selected_tracks = []
        for section in bpm_sections:
            if section["range"][0] <= recommended_bpm <= section["range"][1]:
                selected_tracks = section["tracks"]
                break
        # 구간에 해당하지 않으면 전체 리스트에서 추천
        if not selected_tracks:
            selected_tracks = [track for section in bpm_sections for track in section["tracks"]]

        # 추천 BPM과 가장 가까운 곡 선택
        best_track = min(selected_tracks, key=lambda x: abs(x['bpm'] - recommended_bpm))
        st.info(f"추천 곡: {best_track['name']} (BPM: {best_track['bpm']})")
        st.video(f"https://www.youtube.com/watch?v={best_track['youtube_id']}")
    else:
        st.error('BPM 추천 API 호출 실패')
