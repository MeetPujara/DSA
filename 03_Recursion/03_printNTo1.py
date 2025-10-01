def printNTo1(n):
    if n < 1:
        return
    print(n)
    printNTo1(n-1)

if __name__ == "__main__":
    i = 4
    printNTo1(i)