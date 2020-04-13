def repeatedSubstringPattern(s: str) -> bool:

    divisibleNums = []


    for i in range(1, len(s), 1):
        if (len(s) / i) == int(len(s) / i):
            divisibleNums.append(i) 

    for num in divisibleNums:
        chunks = []
        chunk = ""

        tempS = s
        while len(tempS) > 0:
            chunk = tempS[:num]
            chunks.append(chunk)
            tempS = tempS[num:]
        
        if len(list(set(chunks))) == 1:
            return True
    
    return False

print(repeatedSubstringPattern("bb"))