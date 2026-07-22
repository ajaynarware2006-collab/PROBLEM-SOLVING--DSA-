def firstUniqChar(s):
    s_hash={}
    for i in s:
        if i in s_hash:
            s_hash[i] += 1
        else:
            s_hash[i] = 1
    
    for j in s_hash:
        if s_hash[j] == 1:
            return s.index(j)
    
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))