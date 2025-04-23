'''
Name: Aagam Shah
Roll no: 24BIT194
Batch:H5
Branch: Information and Communication Technology (ICT)
'''

# 1. Count vowels in a user-entered string
text = input("Input a string: ")
vowel_count = 0
for char in text:
    if char in "aeiouAEIOU":
        vowel_count += 1
print("Total vowels:", vowel_count)

# 2. Custom functions for case conversions
string = input("Enter a string for changing case: ")

# To uppercase
to_upper = ""
for char in string:
    if 'a' <= char <= 'z':
        to_upper += chr(ord(char) - 32)
    else:
        to_upper += char
print("Uppercase version:", to_upper)

# To lowercase
to_lower = ""
for char in string:
    if 'A' <= char <= 'Z':
        to_lower += chr(ord(char) + 32)
    else:
        to_lower += char
print("Lowercase version:", to_lower)

# Toggle case
toggle = ""
for char in string:
    if 'A' <= char <= 'Z':
        toggle += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        toggle += chr(ord(char) - 32)
    else:
        toggle += char
print("Toggled case:", toggle)

# 3. Check if one string exists inside another
first_str = input("Enter string one: ")
second_str = input("Enter string two: ")

if first_str in second_str or second_str in first_str:
    print("present")
else:
    print("not present")

# 4. Remove a substring from a main string if it's found
main_string = input("Main string: ")
to_remove = input("Substring to remove: ")

result_str = ""
pos = 0
while pos < len(main_string):
    if main_string[pos:pos+len(to_remove)] == to_remove:
        pos += len(to_remove)
    else:
        result_str += main_string[pos]
        pos += 1
print("Resulting string:", result_str)
