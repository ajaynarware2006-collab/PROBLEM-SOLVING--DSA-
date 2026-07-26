def maxVowels(s, k):
    vowels={
        "a":0,
        "u":0,
        "o":0,
        "i":0,
        "e":0
    }
    count=0
    substring=s[:k]
    for i in substring:
        if i in vowels:
            count += 1

    maxcount = count
    for i in range(k,len(s)):
        if s[i-k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1
 
        maxcount=max(count , maxcount)

    return maxcount


print(maxVowels("abciiidef",3))
print(maxVowels("leetcode",3))
print(maxVowels("aeiou",2))
print(maxVowels("weallloveyou",7))
