def power(x, n):
    if n == 0:
        return 1
    else:
        return power(x, n-1)*x


if __name__=="__main__":

    print(f"power(5, 3) = {power(5, 3)}")
