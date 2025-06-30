def p11(n):
    for i in range(1,n+1):
        if(i%2==0):
            start = 0
        else:
            start = 1
        for j in range(1,i+1):
            print(start,end="")
            start = 1-start
        print()
p11(5)


