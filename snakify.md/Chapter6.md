## List of squares
For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.
```.py
N = int(input())
x = 1

while x**2 < N+1:
    print(x**2)
    x += 1
```
![image](https://user-images.githubusercontent.com/89135778/191248914-5aad1f3e-b346-42d9-a01b-9bd54061d8ea.png)

## Least divisor
Given an integer not less than 2. Print its smallest integer divisor greater than 1.
```.py
number = int(input())
divisor = 2

while number % divisor != 0:
    divisor += 1

print(divisor)
```
![image](https://user-images.githubusercontent.com/89135778/192142280-7796efec-53fa-4bc9-bbbc-f93b6122a097.png)

## The power of two
For a given integer N, find the greatest integer x where 2^x is less than or equal to N. Print the exponent value and the result of the expression 2^x.
```.py
N = int(input())
y = 0
z = 1
while z * 2 <= N:
    y = y + 1 
    z = z * 2
print(y, z)
```
![image](https://user-images.githubusercontent.com/89135778/192142946-0b3eb0fb-6716-4fc6-b28d-3b82956b3a12.png)

## Morning jog
As a future athlete you just started your practice for an upcoming event. Given that on the first day you run x miles, and by the event you must be able to run y miles.
Calculate the number of days required for you to finally reach the required distance for the event, if you increases your distance each day by 10% from the previous day.
Print one integer representing the number of days to reach the required distance.
```.py
miles = int(input())
total_miles = int(input())
days = 1

while miles < total_miles:
    days += 1
    miles += miles*0.1

print(days)
```
![image](https://user-images.githubusercontent.com/89135778/192143594-bd0ea865-f13f-42fe-ad73-fb677d19bc7b.png)

## 
```.py

```

## 
```.py

```
