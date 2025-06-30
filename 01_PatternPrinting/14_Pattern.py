def p14(n):
    for i in range(1,n+1):
        for j in range(ord('A'),ord('A')+i):
            print(chr(j),end=" ")
        print()
p14(5)


