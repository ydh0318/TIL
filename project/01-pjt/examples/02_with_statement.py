# import sys
# print(sys.getdefaultencoding())

# data = open('example.txt', 'r', encoding='utf-8')
data = open('example.txt', 'r')
# print(data)
# print(data.read())
# data.close()

with open('example.txt', 'r') as data:
    print(data)
    print(data.read())
