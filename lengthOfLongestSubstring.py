class Solution:
    def lengthOfLongestSubstring(self, s):
        # dicts = {}
        # maxlength = start = 0
        # for i,value in enumerate(s):
        #     if value in dicts:
        #         repeatedCharIdx = dicts[value] + 1
        #         if repeatedCharIdx > start:
        #             start = repeatedCharIdx
        #     length = i - start + 1
        #     maxlength = max(length, maxlength)
        #     dicts[value] = i
        # return maxlength
        
        
        maxLength = 0
        chars = []
        for char in s:
            if char in chars:
                charIdx = chars.index(char)
                chars = chars[charIdx + 1:]
            
            chars.append(char)
            maxLength = max(len(chars), maxLength)
        
        return maxLength