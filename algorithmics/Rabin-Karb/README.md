# Rabin-Karp Algorithm

The brute force algorithm for string pattern matching has a time complexity of $O(nm)$.

One idea to optimize this is to assign numerical values to characters, treating the string as a number in a base- $d$ system, where $d$ is the size of the alphabet. The process is:
1. Calculate the numerical value for the Pattern (length $m$).
2. In the Text of length $n$, calculate the numerical value for the initial substring (indices 0 to $m-1$).
 3. Iteratively calculate the value for each subsequent substring of length $m$ using a "Rolling Hash".
 4. If the numerical value of a substring matches the Pattern's value, mark it as a match.

 The Problem:
 Theoretically, this reduces complexity to $O(n)$. However, long strings result in numerical values that are too large to fit in standard CPU registers of 64-bit. Storing these values requires an array-like structure (Big Integers). Performing arithmetic operations on these large numbers takes $O(m)$ time. Therefore, the total complexity returns to O(nm).

The Solution (Rabin-Karp):
 While we cannot reduce the worst-case complexity of this specific hashing approach, we can significantly improve the average case.

This is the Rabin-Karp Algorithm. The strategy is to perform all calculations modulo $q$, where $q$ is a prime number that fits in a standard integer.
 *   This keeps the numbers small, making arithmetic $O(1)$.
 *   Matching hash values identifies "candidates."
 *   Since different strings can produce the same hash (collisions), we verify all candidates using brute force.

 Although the worst-case complexity remains $O(nm)$ (if many collisions occur), the average complexity is $O(n+m)$, making it highly efficient for practical use.
