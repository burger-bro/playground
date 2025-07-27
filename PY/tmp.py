import random

start = 1

epoch = 10

for i in range(epoch):
    increment_ratio = 0.1 * random.random() 
    start += start * increment_ratio
    print(f"Epoch {i + 1}: {start:.2f}, Increment Ratio: {increment_ratio:.2f}")

print(start)

