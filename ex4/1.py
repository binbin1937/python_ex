temp = ['A','B','C','D']

for i in range(3):
    temp1 = temp[0]
    temp = temp[1:]
    temp.append(temp1)
    print(temp)