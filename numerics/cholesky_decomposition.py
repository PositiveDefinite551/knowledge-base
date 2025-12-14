import numpy as np

def cholesky_decomposition(A):
    """
    Given a positive definite n*n matrix, in (n**3)*(1+O(1/n))/3 steps returns a n*n lower triangular matrix L, such that L@L^t=A
    
    """
    def cholesky_decomposition(A):
    n = A.shape[0]
    L = np.zeros((n,n), dtype=np.float64)

    for s in range(n):
        
        sigma = 0
        for k in range(s):
            sigma+=(L[s][k])**2
        L[s][s]=(A[s][s]-sigma)**(1/2)

        for i in range(s+1, n):
            sigma = 0
            for k in range(s):
                sigma += L[i][k]*L[s][k]
            L[i][s]=(A[i][s]-sigma)/L[s][s]
            
    return L
