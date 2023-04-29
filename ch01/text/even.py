def even(k):
    print(2*k)
    odd(k)

def odd(k):
    print(2*k-1)
    if not k == 1:
        even(k-1)

def count_2k(k):
    even(k)

if __name__=="__main__":

    print(count_2k(4))
