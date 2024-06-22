def divisiblesofseven(start, end):
    divisible_numbers = []
    total_sum = 0
    for num in range(start, end):
        if num % 7 == 0:
            divisible_numbers.append(num)
            total_sum += num
    return divisible_numbers, total_sum
start_range = 101
end_range = 200
divisible_nums, sum_of_divisibles = divisiblesofseven(start_range, end_range)
print(f"Numbers divisible by 7 between {start_range} and {end_range}: {divisible_nums}")
print(f"Sum of these numbers: {sum_of_divisibles}")
