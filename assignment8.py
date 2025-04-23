'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''
import random

# 1. Convert list of words to uppercase and store in a set
word_list = ["hello", "world", "pdeu", "energy", "university"]
uppercase_words = {word.upper() for word in word_list}
print("Uppercase Set:", uppercase_words)

# 2. Generate 10 random integers from 15–45, count numbers <30, and remove those >35
random_nums = set()
while len(random_nums) < 10:
    random_nums.add(random.randint(15, 45))

print("Initial Set:", random_nums)

less_than_30 = sum(1 for x in random_nums if x < 30)
print("Count of numbers less than 30:", less_than_30)

random_nums -= {x for x in random_nums if x > 35}
print("After removing numbers greater than 35:", random_nums)

# 3. Work with a set of names - add, modify, delete
student_names = set()

# Adding names
for name in ["Ravi", "Amit", "Rohit", "Kiran", "Priya"]:
    student_names.add(name)

# Modifying by removing and adding
student_names.discard("Ravi")
student_names.add("Ravindra")

# Deleting two names
student_names.difference_update({"Kiran", "Amit"})

print("Final set of names:", student_names)

# 4. Divide names into sets A and B based on first letter
all_names = {"Amit", "Anil", "Bhavesh", "Bhavin", "Ajay", "Bharat"}
set_a = {name for name in all_names if name.startswith('A')}
set_b = {name for name in all_names if name.startswith('B')}

print("Names starting with A:", set_a)
print("Names starting with B:", set_b)
