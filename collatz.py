def collatz(n):
    return (n//2 if n%2==0 else 3*n+1)

dp={}
def count_collatz_r(n):
    if n <= 1: 
        return 0
    return count_collatz_r(collatz(n)) + 1

def count_collatz(n):
    count, st, orig = 1, [], n
    while n > 1:
        if n in dp:
            count = dp[n] + 1
            break
        st.append(n)
        n = collatz(n)
    print(orig, st)
    while st:
        dp[st.pop()] = count
        count += 1
    return dp[orig]
    
for i in range(980,1001):
    a, b = count_collatz(i), count_collatz_r(i)
    print(i, '->', a, '(opt)', b, '(unopt)')

