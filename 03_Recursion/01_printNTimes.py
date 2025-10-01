def func(i, n):
    # Base Condition.
    if i > n:
        return
    print("Meet")
    func(i + 1, n)

if __name__ == "__main__":
    n = 4
    func(1, n) 