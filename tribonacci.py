def trib(n):
    if n == 0 or n==1:
        return 0
    if n==2:
        return 1
    return trib(n-1) + trib(n-2) + trib(n-3)
print(trib(15))
# make it faster by memos
def tribo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0 or n==1:
        return 0
    if n==2:
        return 1
    memo[n] = tribo(n-1, memo) + tribo(n-2, memo) + tribo(n-3, memo)
    return memo[n]
print(tribo(15))