# Q6: Sets, Tuples, random, math modules
import random
import math

def number_operations():
    unique_numbers = set()
    print("Enter 10 numbers:")
    
    while len(unique_numbers) < 10:
        try:
            num = int(input(f"Enter number {len(unique_numbers)+1}: "))
            unique_numbers.add(num)
        except ValueError:
            print("Enter valid integer!")
    
    print(f"\nUnique Set: {unique_numbers}")
    
    # Set to Tuple convert kar
    num_tuple = tuple(unique_numbers)
    print(f"Tuple: {num_tuple}")
    
    # 3 random numbers pick kar
    try:
        random_nums = random.sample(num_tuple, 3)
        print(f"3 Random Numbers: {random_nums}")
    except ValueError:
        print("Not enough elements for sampling!")
    
    # Sum cha square root
    total_sum = sum(num_tuple)
    sqrt_sum = math.sqrt(total_sum)
    print(f"Sum of tuple: {total_sum}")
    print(f"Square root of sum: {sqrt_sum:.2f}")

number_operations()