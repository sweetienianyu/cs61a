# learn cs61a
### contains homeworkd, lab, exams, and my note

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
def square(x):
    return x * x
    
def invert(f):
    return lambda y: search(lambda x: f(x) == y)
sqrt = invert(square)
sqrt(16)
```