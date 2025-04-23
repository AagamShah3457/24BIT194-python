'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''


import random
from collections import deque

# 1. Create and manipulate a list of random odd and even numbers
odd_nums = [random.randrange(1, 100, 2) for _ in range(5)]
print("Odd numbers:", odd_nums)

even_nums = [random.randrange(0, 100, 2) for _ in range(4)]
print("Even numbers:", even_nums)

odd_nums[2] = even_nums
print("Modified odd list (3rd replaced):", odd_nums)

# Flatten the nested list
combined = []
for val in odd_nums:
    if isinstance(val, list):
        combined.extend(val)
    else:
        combined.append(val)

print("Flattened list:", combined)

combined.sort()
print("Sorted list:", combined)

# 2. Generate list and find all occurrences of a given value
values = [random.randint(1, 10) for _ in range(20)]
print("Generated values:", values)

search = int(input("Enter number to search: "))
found_indices = [i for i, val in enumerate(values) if val == search]
print("Found at indices:", found_indices)

# 3. Remove duplicates from 50 random numbers
rand_vals = [random.randint(1, 30) for _ in range(50)]
print("Initial values:", rand_vals)

unique_vals = list(set(rand_vals))
print("After duplicate removal:", unique_vals)

# 4. Split numbers into positive and negative
mixed_vals = [random.randint(-50, 50) for _ in range(30)]
pos_list = [x for x in mixed_vals if x >= 0]
neg_list = [x for x in mixed_vals if x < 0]

print("All values:", mixed_vals)
print("Positive numbers:", pos_list)
print("Negative numbers:", neg_list)

# 5. Convert strings to uppercase
words = ["pdeu", "hello", "python", "rocks", "lists"]
upper_words = [w.upper() for w in words]
print("Uppercased:", upper_words)

# 6. Convert temperatures from Fahrenheit to Celsius
fahrenheit = [32, 68, 86, 104, 122]
celsius = [(t - 32) * 5 / 9 for t in fahrenheit]
print("Fahrenheit temps:", fahrenheit)
print("Converted to Celsius:", celsius)

# 7. Stack operations with menu
stack_data = []

while True:
    print("\nStack Menu\n1. Push\n2. Pop\n3. Show\n4. Exit")
    op = input("Choose option: ")
    if op == '1':
        element = input("Push value: ")
        stack_data.append(element)
    elif op == '2':
        if stack_data:
            print("Removed:", stack_data.pop())
        else:
            print("Stack is empty.")
    elif op == '3':
        print("Stack:", stack_data)
    elif op == '4':
        break
    else:
        print("Invalid choice!")

# 8. Queue operations using deque
queue_data = deque()

while True:
    print("\nQueue Menu\n1. Enqueue\n2. Dequeue\n3. Show\n4. Exit")
    option = input("Enter your choice: ")
    if option == '1':
        val = input("Insert value: ")
        queue_data.append(val)
    elif option == '2':
        if queue_data:
            print("Removed:", queue_data.popleft())
        else:
            print("Queue is empty.")
    elif option == '3':
        print("Queue:", list(queue_data))
    elif option == '4':
        break
    else:
        print("Invalid input!")

# 9. Elements in first list not in second
first = [1, 2, 3, 4, 5, 6, 7]
second = [2, 4, 6]
difference = [item for item in first if item not in second]
print("First list:", first)
print("Second list:", second)
print("Only in first:", difference)
