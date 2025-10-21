import math

def e_up(N): 
   """
   Approaches e with a while-loop, N growing
   Args:
       N (int): Number of summation steps

   Returns:
       int: Approximation of Euler's number
   """
  
    n=0
    e=0
    while n<N:
        e+=1/math.factorial(n)
        n+=1
    return e

# Approach e with a while-loop, N falling
def e_down(N):
  """
   Approaches e with a while-loop, N falling
   Args:
       N (int): Number of summation steps

   Returns:
       int: Approximation of Euler's number
   """
  
    e=0
    while N>=0:
        e+= 1/math.factorial(N)
        N=N-1
    return e


N=10
print(e_up(N))
print(e_down(N))

# Explanation as to why the results differ:
# e_up and e_down sum the same terms but in opposite order.
# Floating-point addition is not (perfectly) associative, so summing small
# numbers first (as in e_down) or last (as in e_up) can give differences.
