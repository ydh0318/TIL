import sys

sys.stdin = open('input.txt','r')

# 동철이의 회사에는 N명의 직원이 있다.
# 성공할 확률의 최댓값을 리턴

# 직원 번호와 지금까지의 확률값을 넘겨줌
def probability_maximize(employee, probability):
    global max_probability
    # 가지치기 
    if probability < max_probability: return
    
    # 종료조건
    # 일을 다 선점 했을 때 : 최대값 업데이트
    if employee == N:
        max_probability = max(max_probability, probability)
        return
    
    # 남은 일 중 선점되지 않은 것
    for i in range(N):
        if not is_job_assigned[i]:
            # 성공할 확률이 0이면 건너 뜀 
            if matrix[employee][i] == 0: continue
            is_job_assigned[i] = True
            probability_maximize(employee + 1, probability * matrix[employee][i]/100)
            is_job_assigned[i] = False
    

T = int(input())
for tc in range(1,T+1):
    
    # 사람 수
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_probability = 0

    is_job_assigned = [False] * N
    probability_maximize(0,1)
            
    print(f'#{tc} {max_probability * 100:.6f}')
