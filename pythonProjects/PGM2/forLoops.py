def numberStairs(n):
    for row in range(1, n + 1):
        for column in range(1, row + 1):
            print(column, end = "")
        print()
print(numberStairs(5))