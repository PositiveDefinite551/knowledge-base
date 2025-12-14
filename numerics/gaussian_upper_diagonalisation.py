import numpy as np


def upper_diagonalize(A):
  """
   Performs upper diagonalisation on a matrix
   Args:
       A (ndarray): Matrix to be upper-diagonalised

   Returns:
       ndarray: upper-diagonalised Matrix
   """
    n = A.shape[0]
    z = 0
    s = 0
    while z < n and s<n:
        print(A)
        while A[z,s]==0:
            for i in range(z+1,n):
                if A[i,s]!=0:
                    A[z],A[i]=A[i],A[z]
                    break
            else:
                s+=1
            if s>=n or z>=n:
                break
        if s==n:
            return A
        else:   
            A[z]= A[z]* (1/(A[z,s]))
            for j in range(z+1, n):
                A[j]-=A[j,s]*A[z]
        z+=1
        s+=1
        
    return A
