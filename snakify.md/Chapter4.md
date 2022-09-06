## Count to N
Given an integer N, print all the numbers from 1 to N.
```.py
N = int(input())

for i in range (1, N+1):
    print(i)
```
![image](https://user-images.githubusercontent.com/89135778/188455261-4e57574f-69be-4271-be45-193bcb3cbd47.png)

## Series - 1
Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
```.py
a = int(input())
b = int(input())

for i in range (a, b+1):
    print(i)
```
![image](https://user-images.githubusercontent.com/89135778/188455523-641d0cca-be98-4d8b-a6b7-c8530483006f.png)

## First N odd, ascending
Given an integer N, print all the odd numbers from 1 to N in ascending order.
```.py
N = int(input())

for i in range (1, N+1, 2):
    print(i)
```
![image](https://user-images.githubusercontent.com/89135778/188455832-ce2da140-9a61-4c50-8b57-f6369f533e62.png)

## Series - 2
Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.
```.py
a = int(input())
b = int(input())

if a < b:
    for i in range (a, b+1):
        print(i)

if a > b:
    for i in range (a, b-1, -1):
        print(i)

if a == b:
    print(a)
```
![image](https://user-images.githubusercontent.com/89135778/188456834-7f80a10e-cb33-4329-8382-06477e3851ff.png)

## First N even, descending
Given an integer N, print all the even numbers from 0 to N in descending order.
```.py
n = int(input())

if n % 2 != 0:
    for i in range(n-1, -2, -2):
        print(i)
else:
    for i in range(n, -1, -2):
        print(i)
```
#### Model solution:
```.py
n = int(input())
if n % 2 == 1:
    n -= 1
for i in range(n, -1, -2):
    print(i)
```
![image](https://user-images.githubusercontent.com/89135778/188623289-49b6921a-6c6d-49b4-bef4-43a709a985e8.png)

## Sum of ten numbers
10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.
```.py
sum = 0
for i in range(0, 10):
    num = int(input())
    sum += num
print(sum)
```
![image](https://user-images.githubusercontent.com/89135778/188606565-03e3bda1-8344-4ac6-928e-c9097552ceb0.png)

## Sum of N numbers
N numbers are given in the input. Read them and print their sum.
The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers.
```.py
total_nums = int(input())
sum = 0
for i in range(0, total_nums):
    num = int(input())
    sum += num
print(sum)
```
![image](https://user-images.githubusercontent.com/89135778/188609531-b1a5a497-0a5f-4a29-a1fe-28475a8608ad.png)

## Product of N numbers
N numbers are given in the input. Read them and print their product.
The first line of input contains a positive integer N: the number of integers to follow. Each of the next N lines contains one integer. Print the product of these N integers.
```.py
total_nums = int(input())
prod = 1
for i in range(0, total_nums):
    num = int(input())
    prod *= num
print(prod)
```
![image](https://user-images.githubusercontent.com/89135778/188610924-a2e74188-2dcb-47fa-a761-8982866152a0.png)

## Sum of cubes
For the given integer N calculate the following sum:
1^3+2^3+…+N^3
```.py
N = int(input())
num = 0
sum = 0
for i in range(N+1):
    prod = num**3
    num += 1
    sum += prod
print(sum)
```
![image](https://user-images.githubusercontent.com/89135778/188620535-3ef83112-3173-455e-826b-ed82070f91cb.png)

## Factorial
In mathematics, the factorial of an integer n, denoted by n! is the following product:
n!=1×2×…×n
For the given integer n calculate the value n!. Don't use math module in this exercise.
```.py

```

## The number of zeros
Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equal to zero, not the number of zero digits.
```.py

```

## Adding factorials
Given an integer n, print the sum 1!+2!+3!+...+n!.
This problem has a solution with only one loop, so try to discover it. And don't use the math library :)
```.py

```

## Squares in range
Given two integers A and B, print squares of all integer numbers between them, as shown below. There shouldn't be any spaces around * and =. The sep argument of the function print() may help you with that.
```.py

```

## Ladder
For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.
To do that, you can use the sep and end arguments for the function print().
```.py

```

## Is prime
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given an integer N > 1, print PRIME if it's prime and print COMPOSITE otherwise.
```.py

```

## Print primes in range
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given two integers A and B, print all prime numbers between them, inclusively.
```.py

```

## Number of primes in range
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given two integers A and B, print the number of primes between them, inclusively.
```.py

```

## Lost card
There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.
```.py

```

## 
```.py

```

## 
```.py

```

## 
```.py

```

## 
```.py

```

## 
```.py

```

## 
```.py

```
