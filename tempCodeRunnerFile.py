num = [1,5,7,8]
for i in range(len(num)):
    for j in range(i+1, len(num)):
        add = num[i] + num[j]
        print(i,j) 