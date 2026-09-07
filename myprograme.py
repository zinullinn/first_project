mylist = [64,334,25,12,22,11,90,5]

n = len(mylist)
for i in range (1,n):
    insert_index = i
    current_value = mylist.pop(i)
    for j in range (i-1, -1, -1):
        if mylist[j] > current_value:
            insert_index = j
    mylist.insert(insert_index, current_value)
print(mylist)