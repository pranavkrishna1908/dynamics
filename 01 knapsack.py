weights = [1,4,2,3,5,6,3,1,2,3,4,5,2,1]
profits = [1,2,5,3,6,4,1,6,3,8,5,2,5,8]
limit = 14
def knapsack_slow(limit, weights, profits):
    if limit == 0:
        return 0
    if limit < 0:
        return None
    num = len(weights)
    best_profit = 0
    for index in range(num):
        profit = knapsack_slow(limit - weights[index],
                         weights[:index] + weights[index+1:],
                         profits[:index] + profits[index+1:])
        if profit is not None:
            profit = profit + profits[index]
            if profit > best_profit:
                best_profit = profit
    return best_profit
# print(knapsack_slow(limit, weights, profits))
# but, how to knapsack
def knapsack(limit, weights, profits, memo = {}):
    if (limit, tuple(weights)) in memo:
        return memo[(limit, tuple(weights))]
    if limit == 0:
        memo[(0,tuple(weights))] = 0,[]
        return 0,[]
    if limit < 0:
        memo[(limit,tuple(weights))] = None, None
        return None, None
    num = len(weights)
    best_profit = 0
    best_items = []
    for index in range(num):
        profit, items = knapsack(limit - weights[index],
                         weights[:index] + weights[index+1:],
                         profits[:index] + profits[index+1:])
        if profit is not None:
            profit = profit + profits[index]
            items = items + [weights[index]]
            if profit > best_profit:
                best_profit = profit
                best_items = items
    memo[(limit, tuple(weights))] = best_profit, best_items
    return best_profit, best_items
# print(knapsack(limit, weights, profits))
import cProfile
import re
cProfile.run('knapsack(limit, weights, profits)')
cProfile.run('knapsack_slow(limit, weights, profits)')


        