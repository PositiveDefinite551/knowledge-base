import numpy as np


def qr_decomposition(A : np.ndarray ) -> tuple[np.ndarray] :
    
    """
    Gram-Schmidt Algorithm for calculating the QR-decomposition.
    ---
    Args: 
        A(np.ndarray) : The mxn matrix to decompose
    ---
    Returns:
        tuple[np.ndarray] : Orthogonal matrix Q, upper-diagonal nxn matrix R, such that QR=A.
    """

    n, m = A.shape[0], A.shape[0]
    R = np.zeros(shape=(n,m))
    QQ = np.zeros(shape=(n,m)) # q
    Q =  np.zeros(shape=(n,m)) # q

    for k in range(n):
        for i in range(k): # when k=1, this loop isn't executed
            R[i][k]= (np.transpose(np.conjugate(Q[i]))) @A[:,k]
            
        sigma = 0
        for i in range(k):
            sigma += (np.transpose(np.conjugate(A[:,k])) @ Q[:,i] ) * Q[:,i]
            
        QQ[:,k] = A[:,k] - sigma
        R[k][k] = np.linalg.norm(QQ[:,k])
        Q[:,k] = QQ[:,k]/R[k][k]

    return Q, R
