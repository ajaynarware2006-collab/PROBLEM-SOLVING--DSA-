class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_hash={}
        for i in s:
            if i in s_hash:
                s_hash[i] += 1
            else:
                s_hash[i] = 1
        for j in t:
            if j in s_hash:
                s_hash[j] -= 1
                if s_hash[j] == 0:
                    del s_hash[j]
            
        if s_hash:
            return False
        
        return True