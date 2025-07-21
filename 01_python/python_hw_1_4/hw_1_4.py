'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''
# 모든 학생의 평균 점수를 계산하여 출력하시오.
# 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
# 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
# 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오

# 아래에 코드를 작성하시오.

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eve": 95
}

average_score = sum(students.values()) / len(students)
students_sorted = sorted(students.items(), key=lambda x: x[1], reverse=True)

print(f"평균 점수: {average_score:.2f}")
#80점 이상 학생 출력 리스트컴프리헨션으로
over80_list = [name for name, score in students.items() if score > 80]
print(f"80점 이상 학생: {over80_list}")

# 80점 이상 학생과 점수 출력
over80_list = [x for _, x in students.items() if x > 80]
print(f"80점 이상 점수: {over80_list}")
print("학생 점수 (내림차순):")

for name, score in students_sorted:
    print(f"{name}: {score}")
print("가장 높은 학생과 가장 낮은 학생의 점수차이:", max(students.values()) - min(students.values()))

for name, score in students.items():
    if score < average_score:
        print(f"{name}의 점수는 평균보다 낮습니다: {score}")