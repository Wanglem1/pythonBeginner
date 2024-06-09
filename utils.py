# My way
def largest_num(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    print(max)

# Mosh way
def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max