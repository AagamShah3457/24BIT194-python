'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''


from datetime import date

# 1. Counting boys and girls using name formatting (boys as tuples)
entries = ["Anjali", "Priya", ("Rohan",), "Meena", ("Amit",), "Neha", ("Raj",), "Sonal"]
boys_count = 0
girls_count = 0

for entry in entries:
    if isinstance(entry, tuple):
        boys_count += 1
    else:
        girls_count += 1

print("Total boys:", boys_count)
print("Total girls:", girls_count)

# 2. Separating student details into individual attribute lists
records = [
    (101, "Ravi", 18),
    (102, "Asha", 19),
    (103, "Kunal", 18),
    (104, "Seema", 20)
]

rolls = [rec[0] for rec in records]
student_names = [rec[1] for rec in records]
student_ages = [rec[2] for rec in records]

print("Roll Nos:", rolls)
print("Names:", student_names)
print("Ages:", student_ages)

# 3. Calculate the difference in days between two date values
first_date = (12, 4, 2023)
second_date = (20, 4, 2025)

date_obj1 = date(first_date[2], first_date[1], first_date[0])
date_obj2 = date(second_date[2], second_date[1], second_date[0])

day_gap = (date_obj2 - date_obj1).days
print("Days difference:", day_gap)

# 4. Sorting a menu based on price in descending order
menu = [
    ("Samosa", 20),
    ("Pizza", 150),
    ("Burger", 90),
    ("Vada Pav", 15),
    ("Dosa", 50)
]

menu_sorted = sorted(menu, key=lambda item: item[1], reverse=True)

print("Menu sorted by cost (high to low):")
for food in menu_sorted:
    print(food)

# 5. Filtering out empty tuples from a collection
raw_tuples = [(), (1, 2), (), (3, 4, 5), (), ("a", "b")]
non_empty = [t for t in raw_tuples if t]

print("Filtered non-empty tuples:", non_empty)

# 6. Changing a value in a tuple by conversion
immutable_data = (10, 20, 30)
mod_list = list(immutable_data)
mod_list[1] = 99
updated_tuple = tuple(mod_list)

print("Tuple after update:", updated_tuple)

# 7. Removing an element from a tuple
tuple_data = (5, 10, 15, 20)
temp = list(tuple_data)
temp.pop(2)
final_tuple = tuple(temp)

print("Tuple after deletion:", final_tuple)
