# 사용자 입력 폼 예시
import streamlit as st

def user_input_form():
    target_hr = st.number_input('목표 심박수', min_value=60, max_value=200, value=140)
    target_cadence = st.number_input('목표 케이던스', min_value=100, max_value=220, value=170)
    return target_hr, target_cadence
