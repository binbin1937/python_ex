for i in '神雕侠侣':
    print(i)


while True:
    print('死循环')
    break



#-方法1
students=['小明','小红','小刚']
a = 0
while a <3:
    student1 = students[0]
    students = students[1:]
    students.append(student1)
    print(students)
    a +=1

#-方法2
students = ['小明','小红','小刚']

for i in range(3):
    students1 = students[0]
    students = students[1:]
    students.append(students1)
    print(students)