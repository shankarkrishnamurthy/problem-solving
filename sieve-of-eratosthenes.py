def walk(n):
    prime=[i for i in range(n+1)]
    prime[0],prime[1] = -1, -1
    for i in range(2, n + 1):
        if prime[i] == i:
            for j in range(i * i, n + 1, i):
                if prime[j] == j: prime[j] = i
        print(i, prime)
    pr = [i for i in range(n+1) if i == prime[i]]
    return (prime,pr)
    
sieve, pr = walk(30)
print(len(pr), pr)
