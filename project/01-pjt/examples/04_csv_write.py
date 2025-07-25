import csv

# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['이름', '나이', '직업'])
#     csv_writer.writerow(['홍길동', 30, '개발자'])
#     csv_writer.writerow(['김영희', 25, '디자이너']) 
#     csv_writer.writerow(['이순신', 40, '군인'])
#     csv_writer.writerow(['박지민', 22, '학생'])

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['이름', '나이', '직업']
    csv_writer = csv.DictWriter(file, fieldnames) 
    csv_writer.writeheader()  # 헤더 작성
    csv_writer.writerow({'이름': '홍길동', '나이': 30, '직업': '개발자'})
    csv_writer.writerow({'이름': '김영희', '나이': 25, '직업': '디자이너'})
    csv_writer.writerow({'이름': '이순신', '나이': 40, '직업': '군인'})
    csv_writer.writerow({'이름': '박지민', '나이': 22, '직업': '학생'})