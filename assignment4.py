'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''

# 1. Display uppercase and lowercase English alphabets
for ch in range(65, 91):
    print(chr(ch), end=' ')
print()
for ch in range(97, 123):
    print(chr(ch), end=' ')
print()

# 2. Multiplication table
number = int(input("Enter a number to display table: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 3. Count letters and digits in input
text = input("Enter some text: ")
letters = 0
digits = 0
for ch in text:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        letters += 1
    elif '0' <= ch <= '9':
        digits += 1
print("Letters:", letters)
print("Digits:", digits)

# 4. Check prime, perfect, Armstrong, palindrome, automorphic
val = int(input("Enter value: "))

# Prime check
is_prime = True
if val < 2:
    is_prime = False
else:
    for i in range(2, val):
        if val % i == 0:
            is_prime = False
            break
print("prime" if is_prime else "not prime")

# Perfect number check
sum_factors = 0
for i in range(1, val):
    if val % i == 0:
        sum_factors += i
print("perfect" if sum_factors == val else "not perfect")

# Armstrong number
temp_val = val
armstrong_sum = 0
while temp_val > 0:
    digit = temp_val % 10
    armstrong_sum += digit ** 3
    temp_val //= 10
print("armstrong" if armstrong_sum == val else "not armstrong")

# Palindrome check
original_val = val
reverse_val = 0
while val > 0:
    reverse_val = reverse_val * 10 + (val % 10)
    val //= 10
print("palindrome" if original_val == reverse_val else "not palindrome")

# Automorphic number
squared = original_val * original_val
print("automorphic" if str(squared).endswith(str(original_val)) else "not automorphic")

# 5. Pythagorean triplets for sides ≤ 30
for x in range(1, 31):
    for y in range(x, 31):
        for z in range(y, 31):
            if x*x + y*y == z*z:
                print(x, y, z)

# 6. Display 24-hour format with suffixes
for hr in range(24):
    if hr == 0:
        print("12 Midnight")
    elif hr < 12:
        print(hr, "AM")
    elif hr == 12:
        print("12 Noon")
    else:
        print(hr - 12, "PM")

# 7. Combinations and permutations (nCr and nPr)
n = int(input("Input value of n: "))
r = int(input("Input value of r: "))

fact_n = 1
for i in range(1, n + 1):
    fact_n *= i

fact_r = 1
for i in range(1, r + 1):
    fact_r *= i

fact_nr = 1
for i in range(1, n - r + 1):
    fact_nr *= i

combinations = fact_n // (fact_r * fact_nr)
permutations = fact_n // fact_nr

print("nCr:", combinations)
print("nPr:", permutations)

# 8. Factorial calculation
val = int(input("Enter a number to calculate factorial: "))
factorial = 1
for i in range(1, val + 1):
    factorial *= i
print("factorial:", factorial)

# 9. Print N natural numbers in reverse
limit = int(input("Enter N: "))
for i in range(limit, 0, -1):
    print(i, end=' ')
print()

# 10. Fibonacci sequence
terms = int(input("Enter how many terms in Fibonacci series: "))
f1, f2 = 0, 1
print(f1, end=' ')
if terms > 1:
    print(f2, end=' ')
for _ in range(2, terms):
    f_next = f1 + f2
    print(f_next, end=' ')
    f1 = f2
    f2 = f_next
print()

# 11. Calculate sin(x) using series expansion
angle_deg = float(input("Enter angle in degrees: "))
angle_rad = angle_deg * 3.14159 / 180

result = 0
sign = 1
for n in range(1, 20, 2):
    fact = 1
    for k in range(1, n + 1):
        fact *= k
    result += sign * (angle_rad ** n) / fact
    sign *= -1
print("sin(x):", result)
