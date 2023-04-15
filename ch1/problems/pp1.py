def odd(n, txt):
    if n == 1:
        return txt + " 1"
    elif n > 0:
        if n % 2 == 1:
            return odd(n-2, txt + " " + str(n))
        else:
            return odd(n-1, txt)

if __name__== "__main__":

    print(odd(12, ""))
    print(odd(7, ""))
