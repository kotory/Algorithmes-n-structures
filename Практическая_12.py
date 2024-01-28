import sys

def division(n, b, q = 0):
    if n < b:
        return n, q
    return division(n - b, b, q + 1)

print(division(5, 2))

def recursion(max1, max2):
    try:
        n = int(input())
    except ValueError:
        print("Please enter an integer.")
        sys.exit()

    if n > 0:
        if max1 < n:
            recursion(n, max1)
        elif max2 < n:
            recursion(max1, n)
        else:
            recursion(max1, max2)
    else:
        print(max2)

recursion(0, 0)
