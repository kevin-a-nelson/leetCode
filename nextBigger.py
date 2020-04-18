def next_bigger(n):
    n = str(n)
    n = map(int, n)
    n = list(n)
        
#     59884848459853
#     598848484 59853 # find first decrease when going for right to left
#     598848484 89553 # swap biggest num after 5
#     598848484 8 9553 # sort last bit from smallest to target
#     598848484 8 3559 # 

    idx = -1
    for i in range(len(n) - 1, -1, -1):
        if n[i] > n[i - 1]:
            idx = i - 1
            break
    
    if idx == -1:
        return idx
        
    left = n[:idx]
    right = n[idx:]
    
    head = right[0]
    
    min = float('inf')
    minIdx = None
    for idx, num in enumerate(right):
        if num <= head:
            continue
        if num < min:
            min = num
            minIdx = idx
    
    right[0], right[minIdx] = right[minIdx], right[0]
    
    right = [right[0]] + list(sorted(right[1:]))

    n = left + right

    n = map(str, n)
    n = "".join(n)
    n = int(n)
    return n