import random as r

# num = int(input())
num = r.randint(0, 50)
nums: list[bool] = []

if type(num) is int:
    print(f'input: {num}')

    for i in range(2, num, 1):
        print(i)

        is_prime = num % i == 0
        if is_prime:
            nums.append(False)
        else:
            nums.append(True)

    # for i in nums:
    #     print(i)

    print(f'{num} is sosu-?: {all(nums)}')
