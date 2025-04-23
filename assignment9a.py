'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''
# 1. Functions stored in a list
def func1():
    print("fun called")

def func2():
    print("disp called")

def func3():
    print("msg called")

function_list = [func1, func2, func3]
for fxn in function_list:
    fxn()

# 2. Add corresponding elements of two lists using map + lambda
a = [1, 2, 3, 4, 5, 6]
b = [6, 5, 4, 3, 2, 1]
sum_list = list(map(lambda i, j: i + j, a, b))
print(sum_list)

# 3. Generate 10 random numbers in range -15 to 15 and square them
import random
random_numbers = random.sample(range(-15, 16), 10)
squared_values = list(map(lambda num: num * num, random_numbers))
print(random_numbers)
print(squared_values)

# 4. Check and print palindromes from a list
items = ['noon', 'Python', 'malayalam', 12321]
for val in items:
    val_str = str(val)
    if val_str == val_str[::-1]:
        print(val_str)

# 5. Get names having length greater than 8
all_names = ["Harshvardhan", "Neel", "Siddharth", "Aarav", "Chandraprakash", "Isha", "Meghna"]
filtered_names = list(filter(lambda name: len(name) > 8, all_names))
print(filtered_names)
