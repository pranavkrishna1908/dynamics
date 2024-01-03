##steps
my_list = [1,2,1,100,3,5,7,9,1,4]
def min_cost(my_list):
    costs = list()
    costs.append(0)
    costs.append(0)
    for item in range(2,len(my_list)):
        one_step = costs[item - 1] + my_list[item-1] 
        two_step = costs[item - 2] + my_list[item-2] 
        cost = min(one_step, two_step)
        costs.append(cost)
    return(costs)
print(min_cost(my_list))
#only needed to look at the last two steps, 
#assume that the previous bits have been done already
#now, do using a recursive strategy?
#will be almost the same, as we will look at the last two elements in my_list for each index and figure out from theere
#question 746 in https://www.youtube.com/watch?v=_i4Yxeh5ceQ
