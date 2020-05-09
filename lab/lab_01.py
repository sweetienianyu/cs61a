#links https://cs61a.org/lab/sol-lab01/
def xk(c, d):
 if c == 4:
    return 6
 elif d >= 4:
    return 6 + 7 + c
 else:
    return 25 

assert xk(10, 10) == 23, "result should be 23"
assert xk(10, 6) == 23, "result should be 19"
assert xk(4, 6) == 6, "result should be 6"
assert xk(0, 0) == 25, "result should be 25"



def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothin'")

#  how_big(7) -> return 'big'
# >>> how_big(12) -> output 'huge'
# >>> how_big(1) -> output 'small'
# >>> how_big(-1) -> output 'nothin'


n = 3
while n >= 0:
    n -= 1
    """
      2->1->0
    """
    print(n)

positive = 28
while positive:
  """
   28->25->22->19->16->13->10->7->4->1
   >>> 
  """
  print("positive?", positive)
  positive -= 3