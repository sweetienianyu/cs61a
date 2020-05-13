# learn cs61a
### contains homeworkd, lab, exams, and my note
### high order function
```
higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(g)(2)
```
### how to compose functions
```
def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x * x

def tripple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
```

### self-reference
```
def print_all(x):
    print(x)
    return print_all

print_all(5)(3)(1)

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x + y)
    return next_sum

print_sums(1)(3)(5)
```

### return
```
def search(f):
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while True:
        if f(x):
            return x
        x += 1
        
def square(x):
    return x * x

def invert(f):
    return lambda y: search(lambda x: f(x) == y)
sqrt = invert(square)
sqrt(16)
```