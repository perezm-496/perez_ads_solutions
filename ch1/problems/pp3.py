def combinations(n, k):
    if n == k:
        return 1
    elif k == 0:
        return 1
    else:
        if 0 < k and k < n:
            return combinations(n-1, k-1) + combinations(n-1, k)
        else:
            return None

if __name__=="__main__":
    display_lines = []
    N = 10
    for n in range(N+1):
        line_txt = " "
        for k in range(n+1):
            line_txt += str(combinations(n, k)) + " "
        display_lines.append(line_txt)
        max_len = len(line_txt)
        
    for line in display_lines:
        pad = (max_len - len(line))//2
        print(" "*pad + line)
        
