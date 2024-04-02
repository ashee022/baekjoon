N = int(input())

numbers = input()

if len(numbers) == N:
    total_sum = sum(int(digit) for digit in numbers)
    print(total_sum)
