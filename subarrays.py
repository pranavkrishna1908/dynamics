#given an integer array, find the subarray wiht the largest product
# if everything is positive, we take everything, so, only wirth thinking about, if there is a negative number or zero
# if there is a zero, have two sections, and find the best one
# so, there are only non zero eelments in my array.
# I think in termsof negative peppered in positives, but that won't help. Maybe the largest product is negative
# nah, even if exactly one number is posotive, the largest product is positive.
# if there are two negatives, there is a positive product
# do a sliding window
import numpy as np
np.random.seed(0)
def largest_contiguous_product(input):
    'assumes, no zeroes, otheriwse, spilt it'
    # not doing a sliding window here
    # need to do a sliding window, as if there are more than two negative numbers, it is the only thing which will be efficient
    # not actually, because all numbers are integers, as long as I am multiplying two negative or one positive, the numbers are non decreasing.

    negs = np.argwhere(input < 0).flatten()
    # forgot to check if the frst eemt in=s negative, this is multiplying by
    num = len(negs)
    # if there are eve unmber of negative integers, return the total product, dont even care
    if len(negs) %2 == 0:
        return np.prod(input)
    elif len(negs) == 1:
        temp1 = np.prod(input[: negs])
        temp2 = np.prod(input[negs+1:])
        if temp1 > temp2:
            return input[: negs]
        else:
            return input[negs+1:]
    else:
        temp1 = np.prod(input[: negs[-1]])
        temp2 = np.prod(input[negs[1]:])
        if temp1 > temp2:
            return (input[: negs[-1]], temp1)
        else:
            return (input[negs[1]:], temp2)
input = np.random.randint(-50,50,size = 10)
print(input)
print(largest_contiguous_product(input[np.nonzero(input)]))
# didnt have to use the sliding window methid
