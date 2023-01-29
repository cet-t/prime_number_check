import random as r

# num = int(input())
num = r.randint(0, 10000)
nums: list[bool] = []

if type(num) is int:
    print(f'input: {num}')

    if num < 2:
        pass

    for i in range(2, num, 1):
        is_prime = num % i == 0
        if is_prime:
            nums.append(False)
        else:
            nums.append(True)

    print(f'{num} is sosu-?: {all(nums)}')
