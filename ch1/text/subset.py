def subset(X, S, m, N, k):
    S1 = S.copy()
    S1.add(X[m])
    if sum(S1) == k:
        return S1
    elif m + 1 < N:
        x = subset(X, S1, m+1, N, k)
        if not x == None:
            return x
        x = subset(X, S, m+1, N, k)
        if not x == None:
            return x
        return None
    else:
        return None

if __name__=="__main__":

    print(subset([1, 2, 3, 5],set(), 0, 3, 6))
