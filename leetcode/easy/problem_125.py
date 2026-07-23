def isPalindrome(s):
    p1=0
    p2=len(s)-1
    while p1 < p2:

        if s[p1].isalnum() and s[p2].isalnum():
            if s[p1].lower() != s[p2].lower():
                return False
            
        if not s[p1].isalnum():
            p1 += 1
        
        elif not s[p2].isalnum():
            p2 -= 1

        else:
            p1 += 1
            p2 -= 1

    return True
            

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("0P"))