fibCache = {0: 0, 1: 1}

def fibonacci(n):
    if n in fibCache:
        return fibCache[n]
    
    nFib = fibonacci(n - 1) + fibonacci(n - 2)
    fibCache[n] = nFib
    return nFib