def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

if __name__=="__main__":

    for k in range(10):
        print(f"Lucas {k}: {lucas(k)}")
