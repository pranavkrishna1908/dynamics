# def steps(n):
#     if n == 1:
#         return 1
#     if n==2:
#         return 2
#     # take  step of ength one
#     temp1 = steps(n-1)
#     #take step of length two
#     temp2 =  steps(n-2)
#     return temp1 + temp2
# steps(15)
# optimise with thememo
def steps(n, memo = {}):
    if n == 1:
        return 1
    if n==2:
        return 2
    if n in memo:
        return memo[n]
    # take  step of ength one
    temp1 = steps(n-1, memo)
    #take step of length two
    temp2 =  steps(n-2, memo)
    answer = temp1 + temp2
    memo[n] = answer
    return answer
steps(15)