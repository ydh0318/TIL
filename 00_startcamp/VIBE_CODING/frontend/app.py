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


# 장르 선택 UI 추가
genre = st.selectbox('장르를 선택하세요', ['전체', '팝', '케이팝', '힙합'])

if st.button('추천 음악 보기'):
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

        # 장르별 BPM 구간별 곡 리스트
        genre_tracks = {
            '팝': [
                {"range": (90, 110), "tracks": [
                    {"name": "Ed Sheeran - Shape of You", "bpm": 96, "youtube_id": "JGwWNGJdvx8"},
                    {"name": "Charlie Puth - Attention", "bpm": 100, "youtube_id": "nfs8NYg7yQM"},
                    {"name": "Bruno Mars - Treasure", "bpm": 108, "youtube_id": "nPvuNsRccVw"}
                ]},
                {"range": (111, 125), "tracks": [
                    {"name": "Dua Lipa - Don't Start Now", "bpm": 124, "youtube_id": "oygrmJFKYZY"},
                    {"name": "Lady Gaga - Poker Face", "bpm": 120, "youtube_id": "bESGLojNYSo"}
                ]},
                {"range": (126, 140), "tracks": [
                    {"name": "Ariana Grande - 7 rings", "bpm": 135, "youtube_id": "QYh6mYIJG2Y"}
                ]},
                {"range": (141, 160), "tracks": [
                    {"name": "Dua Lipa - Physical", "bpm": 150, "youtube_id": "9HDEHj2yzew"}
                ]},
                {"range": (161, 180), "tracks": [
                    {"name": "Lady Gaga - Stupid Love", "bpm": 132, "youtube_id": "5L6xyaeiV58"}
                ]}
            ],
            '케이팝': [
                {"range": (90, 110), "tracks": [
                    {"name": "Red Velvet - Psycho", "bpm": 104, "youtube_id": "uR8Mrt1IpXg"}
                ]},
                {"range": (111, 125), "tracks": [
                    {"name": "BTS - Dynamite", "bpm": 114, "youtube_id": "gdZLi9oWNZg"},
                    {"name": "TWICE - Feel Special", "bpm": 120, "youtube_id": "3ymwOvzhwHs"},
                    {"name": "ITZY - WANNABE", "bpm": 122, "youtube_id": "fE2h3lGlOsk"}
                ]},
                {"range": (126, 140), "tracks": [
                    {"name": "NewJeans - Super Shy", "bpm": 128, "youtube_id": "ArmDp-zijuc"},
                    {"name": "IVE - I AM", "bpm": 128, "youtube_id": "6ZUIwj3FgUY"},
                    {"name": "BLACKPINK - DDU-DU DDU-DU", "bpm": 140, "youtube_id": "IHNzOHi8sJs"}
                ]},
                {"range": (141, 160), "tracks": [
                    {"name": "SEVENTEEN - HOT", "bpm": 148, "youtube_id": "VCDWg0ljbFQ"},
                    {"name": "Stray Kids - God's Menu", "bpm": 150, "youtube_id": "TQTlCHxyuu8"}
                ]},
                {"range": (161, 180), "tracks": [
                    {"name": "BTS - Fire", "bpm": 170, "youtube_id": "0lapF4DQPKQ"},
                    {"name": "EXO - Power", "bpm": 174, "youtube_id": "KSH-FVVtTf0"}
                ]}
            ],
            '힙합': [
                {"range": (90, 110), "tracks": [
                    {"name": "Kendrick Lamar - HUMBLE.", "bpm": 110, "youtube_id": "tvTRZJ-4EyI"},
                    {"name": "Post Malone - Wow.", "bpm": 104, "youtube_id": "wXhTHyIgQ_U"}
                ]},
                {"range": (111, 125), "tracks": [
                    {"name": "Drake - God's Plan", "bpm": 120, "youtube_id": "xpVfcZ0ZcFM"}
                ]},
                {"range": (126, 140), "tracks": [
                    {"name": "Megan Thee Stallion - Savage", "bpm": 132, "youtube_id": "hLkT4F6h3Jw"}
                ]},
                {"range": (141, 160), "tracks": [
                    {"name": "Travis Scott - SICKO MODE", "bpm": 155, "youtube_id": "6ONRf7h3Mdk"}
                ]},
                {"range": (161, 180), "tracks": [
                    {"name": "Cardi B - I Like It", "bpm": 136, "youtube_id": "xTlNMmZKwpA"}
                ]}
            ]
        }

        # 전체 장르 리스트
        all_sections = [
            section for genre_list in genre_tracks.values() for section in genre_list
        ]

        # 선택된 장르의 곡 리스트
        if genre == '전체':
            bpm_sections = all_sections
        else:
            bpm_sections = genre_tracks[genre]

        # 추천 BPM이 속한 구간의 곡 리스트 선택
        selected_tracks = []
        for section in bpm_sections:
            if section["range"][0] <= recommended_bpm <= section["range"][1]:
                selected_tracks = section["tracks"]
                break
        if not selected_tracks:
            selected_tracks = [track for section in bpm_sections for track in section["tracks"]]

        # 추천 BPM과 가장 가까운 곡 선택
        best_track = min(selected_tracks, key=lambda x: abs(x['bpm'] - recommended_bpm))
        st.info(f"추천 곡: {best_track['name']} (BPM: {best_track['bpm']})")
        st.video(f"https://www.youtube.com/watch?v={best_track['youtube_id']}")
    else:
        st.error('BPM 추천 API 호출 실패')
