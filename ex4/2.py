list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = list1
for i in list2:
    list3.append(i)

print(list3)
list1.extend(list2)
list1.sort(reverse=True)
print(list1)