def reverse(x):
    reverse_number = 0
    neg = x < 0
    x = abs(x)
    
    while x > 0:
        ld = x % 10
        reverse_number = (reverse_number * 10) + ld
        x = x // 10
    
    if neg:
        reverse_number = -reverse_number
    
    if reverse_number < -2**31 or reverse_number > 2**31 - 1:
        return 0
    
    return reverse_number

print(reverse(122))  
print(reverse(-122)) 
