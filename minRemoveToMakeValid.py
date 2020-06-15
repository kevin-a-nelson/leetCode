class Solution:
    def minRemoveToMakeValid(self, s):
        
        parens = []
        result = ""
        for idx, char in enumerate(s):
            if char != ')' and char != '(':
                result += char
                continue
                
            if parens == [] and char == ')':
                continue

            if parens == [] and char == '(':
                parens.append(char)
                result += char
                continue

            if parens[-1] == '(' and char == ')':
                result += char
                parens.pop()
                continue
               
            parens.append(char)
            result += char
        
        for paren in parens:
            result = result[::-1]
            result = result.replace('(', '', 1)
            result = result[::-1]

        return result

solution = Solution()
print(solution.minRemoveToMakeValid("))(("))