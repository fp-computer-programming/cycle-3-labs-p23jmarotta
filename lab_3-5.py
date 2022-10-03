# Creator JM 9/29/22
import time
import math

start_math = time.perf_counter()
math.pow(2,2)
end_math = time.perf_counter()
elasped = (start_math - end_math)
print(f'Elasped time (math module) = {elasped}')


start_operator = time.perf_counter()
fo = 2**2
end_operator = time.perf_counter()
elasped = (start_operator - end_operator)
print(f'Elasped time (operators) = {elasped}')

# After changing to time.perf_counter, the first process took longer!
