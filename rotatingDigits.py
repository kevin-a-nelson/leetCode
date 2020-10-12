def rotatesToOtherDigit(digits):

        digits = str(digits)
        digitToRotatedDigit = {
            '0': '0',
            '1': '1',
            '2': '5',
            '5': '2',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        rotatedDigits = ""
        for digit in digits:
            if digit not in digitToRotatedDigit:
                return False
            else:
                rotatedDigits += digitToRotatedDigit[digit]
        
        if digits == rotatedDigits:
            return False
        return True

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        numOfRotatedDigits = 0
        for num in range(N + 1):
            if rotatesToOtherDigit(num):
                numOfRotatedDigits += 1

        return numOfRotatedDigits

solution = Solution()
answer = solution.rotatedDigits(2)

print(answer)