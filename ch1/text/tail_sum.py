import tracemalloc

"""
   This python code exemplifies the use of tail recursion
   and uses tracemalloc to show the advantages of tail recursion.
"""

def non_tail_sum(n):
    """
       Returns the sum of integers from 1 to n
       without using tail recursion.
    """
    if n == 1:
        return 1
    else:
        return non_tail_sum(n-1) + n

def tail_sum(n, s):
    """
       Retursn the sum of integers from 1 to n
       using tail recursion.
    """
    if n == 1:
        return n + s
    else:
        return tail_sum(n-1, s + n)
