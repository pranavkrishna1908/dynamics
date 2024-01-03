def fib(n):
    if n == 0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib0(4), fib0(199))
## optimise it now, using memos
def fib0(n, memo = {}):
    if n == 0 or n==1:
        return 1
    if n in memo:
        return memo[n]
    answer =  fib0(n-1, memo) + fib0(n-2,memo)
    memo[n] = answer
    return answer
print(fib0(4), fib0(19))
# optimise using the tabular dynamic programiming 
