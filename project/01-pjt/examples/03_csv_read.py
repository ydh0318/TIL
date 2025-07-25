import csv

with open('users.csv','r',encoding='utf-8') as file:
    # content = file.read()
    # print(content)

    # csv_reader = csv.reader(file)
    # for row in csv_reader:
    #     print(row)
    
    csv_reader = csv.DictReader(file)
    print(csv_reader.fieldnames)  # 헤더 출력
    for row in csv_reader:
        print(row)
        # print(row['id'], row['name'], row['username'], row['email'])