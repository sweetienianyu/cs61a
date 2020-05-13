# coding practice part

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(g)(2)

