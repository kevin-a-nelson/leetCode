

def backspaceCompare(S: str, T: str) -> bool:

    while True:
        while len(S) != 0 and S[0] == '#':
            S = S[1:]

        hashIdx = S.find('#')

        if(hashIdx == -1):
            break
        
        S = S[0 : hashIdx - 1 : ] + S[ hashIdx + 1 :: ]    

    while True:
        while len(T) != 0 and T[0] == '#':
            T = T[1:]

        hashIdx = T.find('#')

        if(hashIdx == -1):
            break
        
        T = T[0 : hashIdx - 1 : ] + T[ hashIdx + 1 :: ]
      
    return S == T


backspaceCompare("j##xfix", "j###xfix")