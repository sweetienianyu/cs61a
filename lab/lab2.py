def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x + y)
    return next_sum

print_sums(1)(3)(5)