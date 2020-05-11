#links https://cs61a.org/lab/sol-lab01/

# coding practice part

# Q7: Falling Factorial
def falling(n, k):
    total, stop = 1, n-k
    while n > stop:
        total, n = total*n, n-1
    return total

# Q8 Double Eights
def double_eights(n):
    prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False



