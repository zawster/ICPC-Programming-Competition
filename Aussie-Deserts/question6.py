filename = "P6_input.txt"
l = ""
count=1
X=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
with open(filename,"r") as f:
    for line in f:
        l += line
        if len(l) > 10 and len(l) < 100:
            for i in X:
                if 'TPE'+i+'RYIE' in l:
                    print("Case "+str(count)+': Yes')
                    y=True
                    l=''
                    break
            for i in X:
                for j in X:
                    if 'TPE'+i+j+'RYIE' in l:
                        print("Case "+str(count)+': Yes')
                        l=''
                        y=True
                        break
            for i in X:
                for j in X:
                    for k in X:
                        if 'TPE'+i+j+k+'RYIE' in l:
                            print("Case "+str(count)+': Yes')
                            l=''
                            y=True
                            break
            if y is not True:
                print ("Case "+str(count)+": No")
            else:
                y=False
        else:
            print ("Case "+str(count)+": No")
        count+=1
