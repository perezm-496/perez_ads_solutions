def count_down(n):
    print(n)
    if n == 0:
        return
    else:
        count_down(n-2)
        return

if __name__=="__main__":
    print("Count down from 8.")
    count_down(8)

    print("Enters infininte recursion.")

    count_down(9)
