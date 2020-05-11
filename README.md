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
