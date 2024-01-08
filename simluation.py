# You have two fair 6−6−sided dice. At each round, you roll both dice and record the upfaces. Find the expected number of rounds you need to perform to observe all 66 faces of the dice.
import numpy as np
from multiprocessing import Pool
def counter(sample):
    die_1 = sample[0]
    die_2 = sample[1]
    found_nums = set()
    i = 0
    while len(list(found_nums))!= 3:
        found_nums.update([die_1[i], die_2[i]])
        i = i + 1
    return i
# num_samples = 5 * 10**4
# np.random.seed(20)
# samples = np.random.randint(1, 4, (num_samples, 2,100))



# temp = [counter(item) for item in samples]
# print(np.array(temp).mean())


# if __name__ == '__main__':
#     with Pool() as pool:
#         results = pool.map(counter, samples)
#         mean_result = np.array(results).mean()
# print(mean_result )
num_samples = 5 * 10**6
np.random.seed(20)
samples = np.random.randint(1, 7, (num_samples,106))

def reward(sample):
    n1 = list(sample).index(5)
    n2 = list(sample).index(6)
    if n2 < n1:
        return 0
    return np.sum(sample[:n1])

temp = [reward(item) for item in samples]
print(np.array(temp).mean())
