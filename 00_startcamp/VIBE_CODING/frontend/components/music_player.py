# 음악 플레이어 UI 예시
import streamlit as st

def music_player(track_name, bpm):
    st.write(f'현재 재생 중: {track_name} (BPM: {bpm})')
