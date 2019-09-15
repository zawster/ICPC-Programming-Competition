counter = 1
with open ("P5_input.txt") as f:
    lst = []
    for val in f.read().split():
        lst.append(int(val))

while (len(lst)):
    
    y = lst[0]
    x = lst[1]
    if y < 1000 and y >= 2:    
        if x <2000 and x >= 1:
            lst.remove(x)
            lst.remove(y)
            matrix = x*[y*[0]]
            
            for i in range(x):
                for j in range(y):
                    num = lst[0]
                    absNum = abs(num)
                    if absNum-1 == j:
                        matrix[i][absNum-1] = num
                        lst.remove(num)
            final = []
            count = 0
            for k in range(y):
                result = 0    
                for i in range(x):
                    result += matrix[i][k]
                final.append(result)

            flag = 0
            for i in final:
                if i > 0:
                    flag = 1
                    print("Case "+str(counter)+": Yes")
                    break
                else:
                    continue
            if flag == 0:
                print("Case "+str(counter)+": No")
            counter += 1