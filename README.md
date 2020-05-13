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


### what is 'curring'
We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument. More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y). Here, g is a higher-order function that takes in a single argument x and returns another function that takes in a single argument y. This transformation is called currying.
```
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h
curried_pow(2)(3)
```