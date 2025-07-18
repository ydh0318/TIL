# BPM-음악 매칭 알고리즘 예시
def recommend_bpm(current_hr, current_cadence, target_hr, target_cadence):
    bpm = (current_hr + current_cadence) / 2
    if abs(bpm - target_hr) > 10:
        bpm = target_hr
    return int(bpm)
