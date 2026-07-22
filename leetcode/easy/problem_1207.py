def uniqueOccurrences(arr):
    s_hash={}
    for i in arr:
        if i in s_hash:
            s_hash[i] += 1
        else:
            s_hash[i] = 1

    if len(set(s_hash.values())) == len(s_hash):
        return True
    
    return False
    
print(uniqueOccurrences([1,2,2,1,1,3,2,2]))