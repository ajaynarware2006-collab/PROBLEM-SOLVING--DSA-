# nums=[4, 2, 4, 1, 2, 4]

# frequency={}
# for i in nums:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1

# print(frequency)

# def twice():
#     frequency={}
#     for i in nums:
#         if i in frequency:
#             frequency[i] += 1

#             if frequency[i]==2:
#                 return i
           
#         else:
#             frequency[i] = 1

# print(twice())

#anagrams
    
def isAnagram( s, t):
    if len(s) != len(t):
        return False

    s_hash={}
    for i in s:
        if i in s_hash:
            s_hash[i] += 1
        else:
            s_hash[i] = 1
    
    print(s_hash)
    for j in t:
        if j in s_hash:
            s_hash[j] -= 1
            print(s_hash)
            if s_hash[j] == 0:
                del s_hash[j]
                print(s_hash)
        
    if s_hash:
        return False
    
    return True

print(isAnagram("anagram","nagaram"))