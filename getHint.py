def getHint(secret: str, guess: str) -> str:
    sameIdx = 0
    diffIdx = 0
    newSecret = ""
    newGuess = ""
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            sameIdx += 1
        else:
            newSecret += secret[i]
            newGuess += guess[i]
            
    for char in newGuess:
        idx = newSecret.find(char)
        
        if idx == -1:
            continue
        
        diffIdx += 1
        
        newSecret = newSecret.replace(char, '', 1)
    
    return f"{sameIdx}A{diffIdx}B"

print(getHint("1807", "7810"))