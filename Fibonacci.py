def fib(n):
    if n == 0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)
## optimise it now, using memos
def fib0(n, memo = {}):
    if n == 0 or n==1:
        return 1
    if n in memo:
        return memo[n]
    answer =  fib0(n-1, memo) + fib0(n-2,memo)
    memo[n] = answer
    return answer
# optimise using the tabular dynamic programiming 

import cProfile
import re
cProfile.run('fib(20)')
cProfile.run('fib0(900)')
