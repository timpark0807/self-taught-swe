class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        
        if v1 > v2 -> return 1
        if v1 < v2 -> return -1
        
        version1 = "7.5.2.4", version2 = "7.5.3"

        v1 = [7, 5, 2]
                       ^
               
        v2 = [7, 5, 2, 0]
                          ^

        1. Handle same length
        2. Handle len(v1) > len(v2)
        3. Handle len(v2) > len(v1)
        4.
        
        """
        v1_is_bigger = 1
        v2_is_bigger = -1
        v1_and_v2_equal = 0
        v1 = version1.split('.')
        v1 = [int(e) for e in v1]
        v2 = version2.split('.')
        v2 = [int(e) for e in v2]
        p1 = 0
        p2 = 0

        # If v1 and v2 are the same length 
        while p1 < len(v1) and p2 < len(v2):
            if v1[p1] == v2[p2]:
                p1 += 1
                p2 += 1
            elif v1[p1] == '0':
                p1 += 1
            elif v2[p2] == '0':
                p2 += 1
            elif v1[p1] > v2[p2]:
                return v1_is_bigger
            elif v1[p1] < v2[p2]:
                return v2_is_bigger

        # If len(v2) < len(v1)
        # If there is number > 0 -> v1 is bigger
        while p1 < len(v1):
            if v1[p1] == '0':
                p1 += 1
            else:
                return v1_is_bigger
            
        # If len(v2) > len(v1)
        # If there is number > 0 -> v2 is bigger
        while p2 < len(v2):
            if v2[p2] == '0':
                p2 += 1
            else:
                return v2_is_bigger

        # If we have gone through all of v1 and v2
        # They are equal 
        if p1 == len(v1) and p2 == len(v2):
            return v1_and_v2_equal
        
s = Solution()
print(s.compareVersion("7.5.2.4", "7.5.3"))
print(s.compareVersion("7.5.2.0", "7.5.2"))
print(s.compareVersion("7.5.2",   "7.5.2.0"))
print(s.compareVersion("1.01", "1.001"))
print(s.compareVersion("1.0",   "1.0.0"))
print(s.compareVersion("0.1",   "1.1"))












        
