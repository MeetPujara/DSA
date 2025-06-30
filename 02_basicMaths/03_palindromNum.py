def reverse_number(x):
    rev_num = 0
    duplicate = x
    
    while x > 0:
        ld = x % 10
        rev_num = (rev_num*10)+ld
        x = x//10
    
    if duplicate == rev_num:
        print("True")
    else:
        print("False")
reverse_number(121)