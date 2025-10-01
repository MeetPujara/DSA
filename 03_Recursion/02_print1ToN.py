def print1toN(i,n):
    if i > n:
        return 
    print(i)
    print1toN(i+1,n)
    
if __name__ == "__main__":
    n = 4
    print1toN(1,n)