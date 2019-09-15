lst = []
matrix1 = []
with open ("P1_input.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if(c != '\n'):
            lst.append(c)
        if(c == '\n' and lst != []):
            matrix1.append(lst)
            lst = []
N = len(matrix1)
def transpose(A,B): 
  
    for i in range(N): 
        for j in range(N): 
            B[i][j] = A[j][i] 

ch = 'B'
stroke = 0
count = 0
for i in matrix1:
    for j in i:
        if j == ch:
            count += 1
        else:
            count = 0
            break
    if count == N:
        stroke += 1
        count = 0

matrix2 = [[0 for x in range(N)] for y in range(N)] 

transpose(matrix1, matrix2)

for i in matrix2:
    for j in i:
        if j == ch:
            count += 1
        else:
            count = 0
            break
    if count == N:
        stroke += 1
        count = 0
print("Case 1: "+str(stroke))
