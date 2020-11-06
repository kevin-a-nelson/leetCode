class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        matchedChars = ""
        
        for char in T:
            if char in S:
                matchedChars += char
            else:
                matchedChars = ""
            
            if len(matchedChars) == len(S):
                T = T.replace(matchedChars, S)
                matchedChars = ""
        
        return T


solution = Solution()

answer = solution.customSortString("cba", "abcd")

print(answer)