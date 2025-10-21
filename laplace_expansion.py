
import timeit
import numpy as np

def um(A,k): 
  """
   Returns submatrix, by removing the first row, k-th column and then stacking the two parts together.
   Args:
       A (ndarray): Matrix 
       k (int): index of the column to be removed

   Returns:
       ndarray: submatrix
   """
    B = A[ 1: , : ]
    C = np.hstack([B[:,:k], B[:,k+1:]])
    return C


def det_lap(A):
    """
   Calculates the determinant of a matrix using Laplace-Expansion recursively
   Args:
       A (ndarray): Matrix 

   Returns:
       int: determinant of A
   """
    n = A.shape[0]
    if n==1:
        return A[0,0]
    s = 0
    for j in range(n):
        s+= ((-1)**(1+j))*A[0,j]*det_lap((um(A, j)))
    return s
    

def mat_test1(n): # Construct a matrix for testing
    M = np.empty(shape=(n,n))
    for i in range(n):
        for j in range(n):
            if i==j:
                M[i,j]=1
            elif j==i-1 or j==i+1:
                M[i,j]=1/2
            else:
                M[i,j]=0
    return M

# Compare runtime
A = mat_test1(10)
execution_time1 = timeit.timeit(lambda: np.linalg.det(A), number =1)
execution_time2 = timeit.timeit(lambda: det_lap(A), number=1)
print("runtime np: ", round(execution_time1,3))
print("runtime lap: ",execution_time2)
