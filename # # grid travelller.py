# # grid travelller
# def grid(m,n):
#     if m==0:
#          return m
#     if n==0:
#          return n
#     if m==1 and n==1:
#          return 1
#     # go one to the right
#     temp1 = grid(m-1,n)
#     # go one down
#     temp2 = grid(m, n-1)
#     answer = temp1 + temp2
#     return answer
# grid(3,3)
# optimise with a memo
# grid travelller
def grid(m,n, memo = {}):
    if m==0:
         return m
    if n==0:
         return n
    if m==1 and n==1:
         return 1
    if (m,n) in memo:
         return memo[(m,n)]
    # go one to the right
    temp1 = grid(m-1,n, memo)
    # go one down
    temp2 = grid(m, n-1, memo)
    answer = temp1 + temp2

    memo[(m,n)] = answer
    return answer
grid(3,3)