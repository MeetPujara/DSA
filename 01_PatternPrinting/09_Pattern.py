def p9(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(2*i-1):
            print("*",end="")
        print()
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(2*i-1):
            print("*",end="")
        print()
p9(5)