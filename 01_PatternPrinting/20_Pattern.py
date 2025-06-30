def p20(n):
    # Top half
    for i in range(1, n + 1):
        # Left stars
        for j in range(i):
            print("*", end=" ")
        # Spaces
        for j in range(2 * (n - i)):
            print(" ", end=" ")
        # Right stars
        for j in range(i):
            print("*", end=" ")
        print()

    # Bottom half
    for i in range(n-1, 0, -1):
        # Left stars
        for j in range(i):
            print("*", end=" ")
        # Spaces
        for j in range(2 * (n - i)):
            print(" ", end=" ")
        # Right stars
        for j in range(i):
            print("*", end=" ")
        print()

p20(5)
