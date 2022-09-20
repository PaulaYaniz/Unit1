## Last digit of integer
Given an integer number, print its last digit.
```.py
a = (input())

print(a[-1])
```
#### Model solution:
```.py
a = int(input())

print(a % 10)
```
![image](https://user-images.githubusercontent.com/89135778/187174029-1fbb9392-ae23-41e4-a47f-e4627c5710b7.png)

## Tens digit
Given an integer. Print its tens digit.
```.py
a = int(input())

print(a // 10 % 10)
```
![image](https://user-images.githubusercontent.com/89135778/187175313-b0126da0-818c-4be0-b935-31ddf9eddde1.png)

## Sum of digits
Given a three-digit number. Find the sum of its digits.
```.py
a = int(input())

a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10

print(a1+a2+a3)
```
![image](https://user-images.githubusercontent.com/89135778/187176099-9ec14c0b-d3d1-4ca3-82d5-b503c03d998e.png)

## Two digits
Given a two-digit number, print its digits separately.
```.py
a = int(input())

dec = a // 10
uni = a % 10

print(dec, uni)
```
![image](https://user-images.githubusercontent.com/89135778/187663483-ebf40739-8e38-47e9-abfd-316602bd6ed5.png)

## Swap digits
Given a two-digit number, swap its digits as shown in the tests below.
```.py
a = int(input())

dec = a // 10
uni = a % 10

print(str(uni)+str(dec))
```

#### Model solution: 
```.py
a = int(input())
tens = a // 10
units = a % 10
print(units * 10 + tens)
```
![image](https://user-images.githubusercontent.com/89135778/187664090-f7733b0b-a511-456c-84d4-73d4fa63662b.png)

## Last two digits
Given an integer number, print its last two digits.
```.py
a = int(input())

dec = a // 10 % 10
uni = a % 10

print(str(dec)+str(uni))
```

#### Model solution:
```.py
print(int(input()) % 100)
```
![image](https://user-images.githubusercontent.com/89135778/187664737-f5b21da4-72d2-4822-9ecc-701b1b957784.png)

## Reverse three digits
Given a three-digit integer number, print its digits in a reversed order.
```.py
a = int(input())

cen = a // 100
dec = a // 10 % 10
uni = a % 10

print(str(uni)+str(dec)+str(cen))
```
![image](https://user-images.githubusercontent.com/89135778/187665382-66cc8ff7-aced-49a5-8bea-697975023c02.png)

## Merge two numbers
Given two two-digit numbers, merge their digits as shown in the tests below.
```.py
a = int(input())
b = int(input())

a_dec = a // 10 % 10
a_uni = a % 10
b_dec = b // 10 % 10
b_uni = b % 10

print(str(a_dec)+str(b_dec)+str(a_uni)+str(b_uni))
```
![image](https://user-images.githubusercontent.com/89135778/187666047-ae3e3e19-fb71-4deb-939c-9826ebe550b4.png)

## Cyclic rotation
Given a four-digit integer number, perform its cyclic rotation by two digits, as shown in the tests below.
```.py
a = int(input())

mil = a // 1000
cen = a // 100 % 10
dec = a // 10 % 10
uni = a % 10

print(str(dec)+str(uni)+str(mil)+str(cen))
```

#### Model solution
```.py
a = int(input())
print(a % 100 * 100 + a // 100)
```
![image](https://user-images.githubusercontent.com/89135778/187667326-32c1f4a8-f9c0-48bd-ac8c-e7a3c8b8cef7.png)

## Fractional part
Given a positive real number, print its fractional part.
```.py
a = float(input())

print(a % 1)
```
#### Model solution:
```.py
x = float(input())
print(x - int(x))
```
![image](https://user-images.githubusercontent.com/89135778/187815766-8ccb7f41-db70-4f19-8b0a-360fc9059dfa.png)

## First digit after decimal point
Given a positive real number, print its first digit to the right of the decimal point.
```.py
x = float(input())
dec = x - int(x)

print(dec * 10 // 1)
```
#### Model solution:
```.py
x = float(input())
print(int(x * 10) % 10)
```
![image](https://user-images.githubusercontent.com/89135778/187816267-2b0cc980-d5a2-4055-8269-93199bfeb4a8.png)

## Car route
A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
```.py
from math import ceil

n = int(input())
m = int(input())

print(ceil(m / n))
```
![image](https://user-images.githubusercontent.com/89135778/187817053-c6d7cac4-3610-480c-b316-99f80252ccca.png)

## Day of week
Let's count the days of the week as follows: 0 - Sunday, 1 - Monday, 2 - Tuesday, ..., 6 - Saturday. Given an integer K in the range 1 to 365, find the number of the day of the week for the K-th day of the year provided that this year's January 1 is Thursday.
```.py

```

## Digital clock
Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).
```.py
n = int(input())

hours = n // 60
minutes = n % 60

print(hours, minutes)
```
![image](https://user-images.githubusercontent.com/89135778/187903330-a777cd51-9b24-4d9b-8c66-9ebff20ded98.png)

## Total cost
A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
```.py
dollars = int(input())
cents = int(input())
num_cupcakes = int(input())

total_dollars = dollars*num_cupcakes
total_dollars2 = cents*num_cupcakes // 100
total_cents = (cents*num_cupcakes) % 100

print(total_dollars+total_dollars2, total_cents)
```
![image](https://user-images.githubusercontent.com/89135778/191228838-417fc223-d086-44ba-a756-afc104a93cdd.png)

## Century
```.py
I DO NOT KNOW HOW TO DO IT
```

## Snail
A snail goes up A feet during the day and falls B feet at night. How long does it take him to go up H feet?
Given three integer numbers H, A and B (A > B), the program should output a number of days.

```.py
h = int(input())
a = int(input())
b = int(input())
count = 1

x = a-b

while a < h:
    a += x
    count += 1

print(count)
```

#### Model solution:
```.py
from math import ceil

h = int(input())
a = int(input())
b = int(input())
print(ceil((h - a) / (a - b)) + 1)
```
![image](https://user-images.githubusercontent.com/89135778/187907496-46459c85-0566-4052-88f9-3a94609b61ea.png)

## CLOCK FACE 1
H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.
```.py
hours = int(input())
minutes = int(input())
seconds = int(input())

total_seconds = hours*3600 + minutes*60 + seconds

angle = (total_seconds*360) / (3600*12)
print(angle)
```
![image](https://user-images.githubusercontent.com/89135778/191229600-b112bb25-a7dd-4ba7-934a-c7aae48be1cf.png)

## CLOCK FACE 2
Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.
```.py
a = float(input())
a = a % 30
angle = (a * 360) / 30

print(angle)
```
![image](https://user-images.githubusercontent.com/89135778/191230269-0ec04bbb-0d65-470a-a802-c585a200d257.png)
