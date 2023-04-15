def square(n):
    if n == 1:
        return 1
    else:
        return prod(n) + n

def prod(n):
    """
    This function returns n*(n-1)
    using a square as an auxiliary function.
    """
    if n == 1:
        return 0
    else:
        return square(n-1) + n - 1

if __name__=="__main__":

    print(square(3))
