class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)
        
        wordChain = {}
        longestChain = 0
        
        for word in words:
            
            if word not in wordChain:
                wordChain[word] = 1
            
            for i in range(0, len(word)):
                subword = word[:i] + word[i + 1:]
                if subword in wordChain:
                    wordChain[word] = max(wordChain[subword] + 1, wordChain[word])
            
            longestChain = max(longestChain, wordChain[word])
        
        return longestChain
        
        
        
        