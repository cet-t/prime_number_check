import random as r

# num = int(input())
# 10000個目の素数が104729
# num = r.randint(0, 104729)
num = 57
nums: list[bool] = []

print(f'input: {num}')
if num < 2:
    pass

for i in range(2, num, 1):
    is_prime = num % i == 0
    if is_prime:
        nums.append(False)
    else:
        nums.append(True)
    pass


print(f'{num} is sosu-?: {all(nums)}')
