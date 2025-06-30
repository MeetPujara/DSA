def p18(n):
    for i in range(1, n + 1):
        start = ord('A') + n - i 
        for j in range(start, ord('E') + 1):
            print(chr(j), end=" ")
        print()
p18(5)