'''
Name: Aagam Shah
Roll no: 24BIT194
Batch: H5
Branch: Information and Communication Technology (ICT)
'''


# 1. Largest and smallest of two numbers
x = 10
y = 20
if x > y:
    print("largest:", x)
    print("smallest:", y)
else:
    print("largest:", y)
    print("smallest:", x)

# 2. Largest and smallest of three numbers
x = 10
y = 30
z = 20

if x >= y and x >= z:
    max_val = x
elif y >= z:
    max_val = y
else:
    max_val = z

if x <= y and x <= z:
    min_val = x
elif y <= z:
    min_val = y
else:
    min_val = z

print("largest:", max_val)
print("smallest:", min_val)

# 3. Odd or Even
val = 7
if val % 2 == 0:
    print("even")
else:
    print("odd")

# 4. Divisible by 10 or not
val = 50
if val % 10 == 0:
    print("divisible")
else:
    print("not divisible")

# 5. Age check (minor/major)
age = 17
if age < 18:
    print("minor")
else:
    print("major")

# 6. Number of digits in a number
num = 12345
digits = str(num)
print(len(digits))

# 7. Leap year check
yr = 2024
if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

# 8. Valid triangle check (sum of angles = 180)
a1 = 60
a2 = 60
a3 = 60
if a1 + a2 + a3 == 180:
    print("valid")
else:
    print("invalid")

# 9. Absolute value
val = -25
if val < 0:
    print(-val)
else:
    print(val)

# 10. Area vs Perimeter of rectangle
length = 10
width = 5
area = length * width
peri = 2 * (length + width)
if area > peri:
    print("area greater")
else:
    print("perimeter greater or equal")

# 11. Check if 3 points lie on a straight line
x1, y1 = 0, 0
x2, y2 = 2, 2
x3, y3 = 4, 4
if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("straight line")
else:
    print("not on line")

# 12. Point inside/on/outside circle
import math
x, y = 3, 4
cx, cy = 0, 0
r = 5
d = ((x - cx)**2 + (y - cy)**2)**0.5
if d < r:
    print("inside")
elif d == r:
    print("on")
else:
    print("outside")

# 13. 0 to 19 to words using match-case
num = 17
match num:
    case 0: print("zero")
    case 1: print("one")
    case 2: print("two")
    case 3: print("three")
    case 4: print("four")
    case 5: print("five")
    case 6: print("six")
    case 7: print("seven")
    case 8: print("eight")
    case 9: print("nine")
    case 10: print("ten")
    case 11: print("eleven")
    case 12: print("twelve")
    case 13: print("thirteen")
    case 14: print("fourteen")
    case 15: print("fifteen")
    case 16: print("sixteen")
    case 17: print("seventeen")
    case 18: print("eighteen")
    case 19: print("nineteen")
    case _: print("out of range")

# 14. Marks, total, average, pass/fail, grade using if-else
m1 = 75
m2 = 65
m3 = 38
total = m1 + m2 + m3
avg = total / 3
print("total:", total)
print("average:", avg)

if m1 < 40 or m2 < 40 or m3 < 40:
    print("fail")
else:
    print("pass")

# Grade for m1
if m1 == "Absent":
    print("NA")
elif m1 <= 39:
    print("F")
elif m1 <= 44:
    print("P")
elif m1 <= 49:
    print("C")
elif m1 <= 54:
    print("B")
elif m1 <= 59:
    print("B+")
elif m1 <= 69:
    print("A")
elif m1 <= 79:
    print("A+")
elif m1 <= 100:
    print("O")
else:
    print("Invalid")

# Grade for m2
if m2 == "Absent":
    print("NA")
elif m2 <= 39:
    print("F")
elif m2 <= 44:
    print("P")
elif m2 <= 49:
    print("C")
elif m2 <= 54:
    print("B")
elif m2 <= 59:
    print("B+")
elif m2 <= 69:
    print("A")
elif m2 <= 79:
    print("A+")
elif m2 <= 100:
    print("O")
else:
    print("Invalid")

# Grade for m3
if m3 == "Absent":
    print("NA")
elif m3 <= 39:
    print("F")
elif m3 <= 44:
    print("P")
elif m3 <= 49:
    print("C")
elif m3 <= 54:
    print("B")
elif m3 <= 59:
    print("B+")
elif m3 <= 69:
    print("A")
elif m3 <= 79:
    print("A+")
elif m3 <= 100:
    print("O")
else:
    print("Invalid")
