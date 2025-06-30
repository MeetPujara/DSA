def print_pattern_line(stars, spaces):
    print("* " * stars, end="")
    print("  " * spaces, end="")
    print("* " * stars)

def p19(n):
    space = 0
    for i in range(n, 0, -1):
        print_pattern_line(i, space)
        space += 2

    space -= 2
    for i in range(1, n + 1):
        print_pattern_line(i, space)
        space -= 2
p19(5)
