Small code snippets for solving numerical problems and exploring tools for math-related programming.
All the snippets solve their own problem and are unconnected to each other:

`cholesky_decomposition.py` : Given a positive definite $n\times n$ matrix $A$, in $\frac{n^3}{3}(1+O(1/n))$ steps returns a n*n lower triangular matrix $L$, such that $LL^t=A$.

`euler_number.py` : Approximates the Euler's number by summing from above and below. The goal is to compare numerical stability of the methods.

`gaussian_mask.py`: Demonstrates frequency-domain denoising with a Gaussian low-pass filter.

`gaussian_upper_diagonalisation.py`: Performs upper diagonalisation on a matrix

`laplace_expansion.py`: Implements Laplace Expansion for calculating determinant of a given matrix.  The goal is to compare the runtime with a standart approach.

`orthogonal_basis.py`: Find orthogonal basis for a set of vectors.
