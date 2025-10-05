lst = [3, -4, 7, 8, 0, 5, 2, -6, 9, 10] 

for i in range(len(lst)):   
    if lst[i] < 0:           
        lst[i] = 0         

print("Новий список:", lst)

