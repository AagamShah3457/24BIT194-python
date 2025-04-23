'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''
# 1. Count uppercase and lowercase characters
def count_case(text):
    result = {"upper": 0, "lower": 0}
    for char in text:
        if char.isupper():
            result["upper"] += 1
        elif char.islower():
            result["lower"] += 1
    return result

print("Case Count:", count_case("PDEU Rocks at ICT Dept"))

# 2. Compute n + nn + nnn + nnnn
def pattern_sum(n):
    s = str(n)
    return sum(int(s * i) for i in range(1, 5))

for num in range(4, 8):
    print(f"{num} -> {pattern_sum(num)}")

# 3. Create a 3D array with given value
def create_3d_array(x, y, z, val):
    return [[[val for _ in range(z)] for _ in range(y)] for _ in range(x)]

print("3D Array:", create_3d_array(2, 2, 2, 7))

# 4. Calculate sum and average of 5 numbers
def sum_and_avg(*marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

print("Total and Average:", sum_and_avg(70, 80, 60, 90, 75))

# 5. Check if a string is a pangram
def is_pangram(text):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(text.lower())

print("Is Pangram:", is_pangram("The quick brown fox jumps over the lazy dog"))

# 6. Create a list of tuples (x, x², x³)
def powers_up_to(n):
    return [(x, x**2, x**3) for x in range(1, n + 1)]

print("Power List:", powers_up_to(5))

# 7. Check for palindrome (ignoring spaces and case)
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print("Is Palindrome:", is_palindrome("A man a plan a canal Panama"))

# 8. Remove duplicates and sort words in a string
def clean_and_sort(text):
    return " ".join(sorted(set(text.split())))

print("Sorted Unique Words:", clean_and_sort("pdeu ict ict rocks pdeu rocks python"))

# 9. Count alphabets and digits
def count_alpha_num(text):
    result = {"alpha": 0, "digit": 0}
    for char in text:
        if char.isalpha():
            result["alpha"] += 1
        elif char.isdigit():
            result["digit"] += 1
    return result

print("Alpha & Digit Count:", count_alpha_num("ICT2025PDEU42"))

# 10. Frequency of words in a string
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items()))

print("Word Frequency:", word_frequency("the quick brown fox jumps over the lazy dog the quick fox"))

# 11. Intersection of two lists
def list_intersection(l1, l2):
    return [x for x in l1 if x in l2]

print("List Intersection:", list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))


# --- Recursive Functions ---

# 1. Recursive prime factorization
def recursive_factors(n, i=2):
    if i > n:
        return
    if n % i == 0:
        print(i)
        return recursive_factors(n // i, i)
    return recursive_factors(n, i + 1)

print("Prime Factors of 180:")
recursive_factors(180)

# 2. Convert number to binary (recursively)
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

print("Binary of 25:", to_binary(25))

# 3. Count vowels recursively
def count_vowels_recursive(s):
    if not s:
        return 0
    return (s[0].lower() in "aeiou") + count_vowels_recursive(s[1:])

print("Vowel Count:", count_vowels_recursive("PDEU Rocks With Energy"))

# 4. Reverse a list recursively
def reverse_recursively(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_recursively(lst[:-1])

print("Reversed List:", reverse_recursively([1, 2, 3, 4, 5]))

# 5. Recursive power function (a^b)
def power_recursive(a, b):
    if b == 0:
        return 1
    return a * power_recursive(a, b - 1)

print("2^5:", power_recursive(2, 5))

# 6. Replace negative numbers in list with 0 (recursive)
def replace_negatives(lst, i=0):
    if i >= len(lst):
        return lst
    if lst[i] < 0:
        lst[i] = 0
    return replace_negatives(lst, i + 1)

print("Sanitized List:", replace_negatives([-2, 3, -5, 6, -1]))

# 7. Average of list (recursively)
def recursive_average(lst, i=0, total=0):
    if i == len(lst):
        return total / len(lst)
    return recursive_average(lst, i + 1, total + lst[i])

print("Recursive Average:", recursive_average([10, 20, 30, 40, 50]))

# 8. Length of string using recursion
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

print("String Length:", string_length("PDEU"))
