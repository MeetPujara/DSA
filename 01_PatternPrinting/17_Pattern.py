def p17(n):
    for i in range(1,n+1):
        ch = chr(ord('A') + i-1)
        for j in range(n-i):
            print(" ",end="")
        for j in range(0,i):
            print(chr(ord('A')+j),end="")
        for j in range(i-2, -1, -1):
            print(chr(ord('A') + j), end="")
        print()
p17(5)