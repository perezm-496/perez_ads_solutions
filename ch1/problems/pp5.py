def reverse(X, N, txt):
    txt += " " + str(X[N-1])
    if N == 1:
        return txt
    else:
        return reverse(X, N-1, txt)

X = [1, 2, 3, 4, 5]
N = len(X)
print(reverse(X, N, ""))
