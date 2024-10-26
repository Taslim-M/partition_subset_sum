from partition import partition_helper
import time
import random

# def generate_even_numbers(n):
#     return [2 * i for i in range(n)]


def generate_random_even_numbers(n):
    even_numbers = [random.randint(0, 50) * 2 for _ in range(n)]
    return even_numbers

# Example usage
n = 5
print(generate_random_even_numbers(n))  # Output: [random even numbers]


def main():
    n_vals = [10, 100, 200, 300, 400, 500, 1000]
    times = []
    target_sum = []
    for n in n_vals:
        print(n)
        arr = generate_random_even_numbers(n)
        target =  sum(arr)//2
        target_sum.append(target)

        time_start = time.time()
        result = partition_helper(arr)
        times.append(time.time() - time_start)

    print(n_vals)
    print(target_sum)
    print(times)

main()
