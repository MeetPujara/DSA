def p1(n):
    for i in range(n): #outer loop(rows)
        for j in range(n): #inner loop(columns)
            print("*",end=" ")
        print() #moves to next line after each row
        
p1(10)


# for i in range(1,6): # Outer loop for rows

#     for j in range(1,6): # Inner loop for columns
#         print("*",end=" ")
#     print("") # Move to next line after each row