def fibonacci(n):
  '''
  This function takes in an integer value (n) and returns the value of the nth position of the Fibonacci Sequence.

  Input: int n
  Output: int ret_value
  '''

  #if n < 0 then it is not in range of Fib Sequence
  if n <= 0:
    raise ValueError("Out of Range of Fibonacci Sequence. n must be greater than 0")
  #if n is 1st position, the n will always be 0
  elif n == 1:
    return 0
  #if n is 2nd position, the n will always be 1
  elif n == 2:
    return 1
  #if n > 2, use recursion to add previous 2 values of n until sum is totaled
  else:
    ret_value = fibonacci(n-1) + fibonacci(n-2)
    return ret_value


def lucas(n):
  '''
  This function takes in an integer value (n) and returns the value of the nth position of the Lucas Sequence.

  Input: int n
  Output: int ret_value
  '''

   #if n < 0 then it is not in range of Lucas Sequence
  if n <= 0:
    raise ValueError("Out of Range of Lucas Sequence. n must be greater than 0")
  #if n is 1st or 2nd position, the n will always be 2
  elif n == 1:
    return 2
  #if n is 2nd position, the n will always be 1
  elif n == 2:
    return 1
  #if n > 2, use recursion to add previous 2 values of n until sum is totaled
  else:
    ret_value = lucas(n-1) + lucas(n-2)
    return ret_value

def sum_series(n, val1 = 0, val2 = 1):
  '''
  This function takes in an integer value (n) and returns the value of the nth position of a Custom Sequence. There are 2 optional integer values of val1 and val2 which determine the 1st and 2nd positions of the sequence.

  Input: int n
  Optional Input: int val1(default 0), int val2(default 1)
  Output: int ret_value
  '''

  #if n < 0 then it is not in range of Lucas Sequence
  if n <= 0:
    raise ValueError("Out of Range of Current Sequence. n must be greater than 0")
  #if n is 1st or 2nd position, the n will always be val1(default = 0)
  elif n == 1:
    return val1
  #if n is 1st or 2nd position, the n will always be val2(default = 1)
  elif n == 2:
    return val2
  #if n > 2, use recursion to add previous 2 values of n until sum is totaled
  else:
    ret_value = sum_series(n-1, val1, val2) + sum_series(n-2, val1, val2)
    return ret_value

print(f'Fib: {fibonacci(10)}\n')
print(f'Lucas: {lucas(1)}\n')
print(f'Sum: {sum_series(3, 5, 9)}')

