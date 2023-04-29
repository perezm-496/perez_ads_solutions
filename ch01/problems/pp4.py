def palindrome(txt):
    n = len(txt)
    if n == 0:
        return True
    else:
        if not txt[0] == txt[n-1]:
            return False
        return palindrome(txt[1:n-1])
        

if __name__=="__main__":
    test_words = ["x",
                  "x1",
                  "xx",
                  "x1x",
                  "x1y",
                  "abcd1dcba",
                  "1aaa2"]
    for wrd in test_words:
        if palindrome(wrd):
            print(f"{wrd} is a palindrome.")
        else:
            print(f"{wrd} is NOT a palindrome.")
            
