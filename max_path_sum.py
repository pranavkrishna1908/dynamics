import numpy as np
array1 = [
    [1,2,5],
    [6,3,5]
]
costs = np.array(array1)
print(costs)
#now, for this, it is best to use the grid strategy.
final = np.zeros_like(costs)
final[:,0] = np.cumsum(costs[:,0])
final[0,:] = np.cumsum(costs[0,:])
for y in range(1,final.shape[1]):
    for x in range(1,final.shape[0]):
        temp1 = final[x-1, y] + costs[x,y]
        temp2 = final[x,y-1] + costs[x,y]
        best = max(temp1,temp2) 
        final[x,y] = best
print(final)

