# CHAPTER 1: Input, print and numbers

## Sum of three numbers
Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
```.py
a = int(input())
b = int(input())
c = int(input())

print(a + b + c)
```
![image](https://user-images.githubusercontent.com/89135778/187026205-802fee40-f57b-43c2-bb11-2f38edbfc6a3.png)

## Hi John
Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.
```.py
name = input()

print("Hi", name)
```
![image](https://user-images.githubusercontent.com/89135778/187026299-989e3627-9339-4da8-aba1-f7135968082f.png)

## Square
Write a program that takes a number and print its square.
```.py
number = int(input())

print(number ** 2)
```
![image](https://user-images.githubusercontent.com/89135778/187026379-875c6f1f-327a-4ee8-af2f-3383caee80fa.png)

## Area of right-angled triangle
Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.
```.py
b = int(input())
h = int(input())

print((b*h)/2)
```
![image](https://user-images.githubusercontent.com/89135778/187026435-a0d25f9f-624f-4210-9d9e-311371bce7e1.png)

## Hello, Harry!
Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. See the examples below.
```.py
name = input()

print("Hello,", name + "!")
```
![image](https://user-images.githubusercontent.com/89135778/187026469-7723b475-cde8-45e8-bb79-dbf818cb93dc.png)

## Apple sharing
N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?

The program reads the numbers N and K. It should print the two answers for the questions above.
```.py
n = int(input())
k = int(input())

print(k//n)
print(k%n)
```
![image](https://user-images.githubusercontent.com/89135778/187026613-f9a3eada-01e5-4979-a777-469005430ab0.png)

## Previous and next
Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.

Remember that you can convert the numbers to strings using the function str.
```.py
a = int(input())
next = a+1
previous = a-1

print("The next number for the number", a,"is", next)
print("The previous number for the number", a, "is", previous)
```
![image](https://user-images.githubusercontent.com/89135778/187026661-03347225-9beb-4b9e-8081-a39e01f6256f.png)

#### Model solution:
```.py
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')
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























