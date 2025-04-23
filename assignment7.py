'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''


# 1. Merging multiple dictionaries into one
dict1 = {1: 'A', 2: 'B'}
dict2 = {3: 'C', 4: 'D'}
dict3 = {5: 'E'}

merged_dict = {}
merged_dict.update(dict1)
merged_dict.update(dict2)
merged_dict.update(dict3)

print("Combined dictionary:", merged_dict)

# 2. Check if dictionary is empty or not
sample_dict = {}
if sample_dict == {}:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

# 3. Find minimum and maximum salary department-wise
dept_salaries = {
    101: {1: 25000, 2: 30000},
    102: {3: 40000, 4: 28000},
    103: {5: 35000, 6: 45000}
}

for dept_id, employee_sals in dept_salaries.items():
    salaries = employee_sals.values()
    print(f"Department {dept_id} -> Min: {min(salaries)}, Max: {max(salaries)}")

# 4. Calculate character frequency in a string
text = input("Enter text to analyze: ")
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("Character frequencies:", char_count)

# 5. Compute total cost from price and quantity dictionaries
item_prices = {"rice": 60, "wheat": 40, "milk": 25}
item_quantities = {"rice": 2, "wheat": 3, "milk": 5}

bill_total = sum(item_prices[item] * item_quantities.get(item, 0) for item in item_prices)

print("Total bill amount:", bill_total)
