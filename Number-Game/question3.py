def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


def final(var1,var2):
    if is_prime(var1) == True:
        if  is_prime(var2) == True:
            
            return var1+var2
        else:
            return var1 * var2
    else:
        return "not possible"
   

f = open("P3_input.txt")
t = int(f.readline())
for i in range(t):
    temp = f.readline()
    temp = temp.split(' ')
    temp1 = temp[len(temp)-1].split('\n')
    temp[len(temp)-1] = temp1[0]
    
    x = final(int(temp[0]), int(temp[1]))
    st1 = "Case# "+str(i)+": "+str(x)+"\n"
    print(st1)
f.close()