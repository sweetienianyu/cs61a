def print_all(x):
    print(x)
    return print_all
  

print_all(5)(3)(1)