import itertools

class Solution(object):

    def expressiveWords(S, words):
        def RLE(S):
            
            arr = []
            for char, chars in itertools.groupby(S):
                charCount = len(list(chars))
                arr.append((char, charCount))

            chars, charCount = zip(*arr)
            return chars, charCount

        R, count = RLE(S)

        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue

            sameWord = True
            for c1, c2 in zip(count, count2):
                if c1 < max(c2, 3) and c1 != c2:
                    sameWord = False
                    break
            
            if sameWord: ans += 1

        return ans

solution = Solution

# solution.hello()
solution.expressiveWords("heeellooo", ["hello"])