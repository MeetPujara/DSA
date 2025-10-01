def addi(n):
    sum_num = 0
    for i in range(1,n+1):
        sum_num +=i
    return sum_num
# print(addi(5))

def using_recursion(i,sum):
    if i < 1:
        print(sum)
        return
    using_recursion(i-1,sum+i)
    
if __name__ == "__main__":
    n = 5
    using_recursion(n,0)