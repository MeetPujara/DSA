def product(n):
    if n <= 0:
        return 1
    else:
        return n * product(n-1) 
print(product(5))