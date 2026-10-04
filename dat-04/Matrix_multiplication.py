import numpy as np

cricketers = np.array([
    [9,3,7,8], 
    [2,10,6,9], 
    [8,2,6,7]
])

ideal_captain = np.array([8, 5, 7, 9])
names = ['Virat', 'Bumrah', 'Rohit']
print("one ata atime (loop):")
for i, name in enumerate(names):
    score = 0
    for j  in range(4):
        score += cricketers[i][j] * ideal_captain[j]
    print(f"{name}: {score}")
# Virat: 208
# Bumrah: 189
# Rohit: 179 

print("\n All at once(Matrix)")
all_scores = cricketers @ ideal_captain
for name, score in zip(names, all_scores):
    print(f"{name}: {score}")


import time
vocab_size = 100_000
dimensions = 4096

vocabulary = np.random.randn(vocab_size, dimensions).astype(np.float32) 
requirements =  np.random.randn( dimensions).astype(np.float32) 

print(vocabulary) 
print(requirements) #[-0.4792634  -0.72938025  0.11599353 ... -0.91533685 -0.27123973  0.11706407]
print(len(requirements))
start = time.time()

scores_slow = []

for i in range(vocab_size):
    score = 0
    for j  in range(dimensions):
        score+=vocabulary[i][j] * requirements[j]
    scores_slow.append(score)
loop_time = time.time()-start #The loop time  is:  349.8872125148773
print(f"The loop time  is: {loop_time}")
scores_fast = vocabulary @ requirements
matrix_time = time.time()-start
print(matrix_time) 
