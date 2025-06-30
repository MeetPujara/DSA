def armstrong_num(x):
    sum_num = 0
    duplicate_num = x
    while x > 0:
        ld = x % 10
        sum_num = sum_num + (ld*ld*ld)
        x = x//10
    
    if duplicate_num == sum_num:
        print("True")
    else:
        print("False")

 
armstrong_num(370)