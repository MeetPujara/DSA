def p16(n):
    for i in range(1,n+1):
        ch = chr(ord('A') + i - 1)
        for j in range(i):
            print(ch,end="")
        print()
p16(5)