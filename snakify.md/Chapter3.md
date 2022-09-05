## Is positive
Given an integer, print "YES" if it's positive and print "NO" otherwise.
```.py
a = int(input())

if a >= 0:
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/187909454-90a99293-0f13-4ff8-a688-eadfab819b04.png)

## Is odd
Given an integer, print "YES" if it's odd and print "NO" otherwise.
```.py
num = int(input())

if not(num % 2 == 0):
    print("YES")

else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/188259324-3fa09a6a-9b82-449e-a023-fcd6b4645e58.png)

## Is even
Given an integer, print "YES" if it's even and print "NO" otherwise.
```.py
num = int(input())

if num % 2 == 0:
    print("YES")

else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/188259377-b37f18cb-3a5a-402e-85f6-6ecf46190f43.png)

## Ends on seven
Given an integer, print "YES" if it's last digit is 7 and print "NO" otherwise. 
```.py
a = (input())

last = a[-1]

if last == "7":
    print("YES")
else:
    print("NO")
```
#### Model solution:
```.py
if int(input()) % 10 == 7:
    print('YES')
else:
    print('NO')
```
![image](https://user-images.githubusercontent.com/89135778/187912297-7098665f-5d94-481c-a643-d1c9e1f0b215.png)

## Minimum of two numbers
Given two integers, print the smaller value.
```.py
a = int(input())
b = int(input())

if a < b:
    print(a)

else:
    print(b)
```
![image](https://user-images.githubusercontent.com/89135778/187913009-79f574b8-f637-40b0-8091-5531d61c5727.png)

## Are both odd
Given two integers, print "YES" if they're both odd and print "NO" otherwise.
```.py
num1 = int(input())
num2 = int(input())

if num1 % 2 == 1 and num2 % 2 == 1:
    print("YES")

else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/188259523-8b1a9192-92a4-4248-9659-88146e87b3f5.png)

## At leat one odd
Given two integers, print "YES" if at least one of them is odd and print "NO" otherwise.
```.py
num1 = int(input())
num2 = int(input())

if num1 % 2 == 1 or num2 % 2 == 1:
    print("YES")

else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/188259828-7921bc99-5064-4d68-948d-882bc087445c.png)

## Exactly one odd
Given two integers, print "YES" if exactly one of them is odd and print "NO" otherwise.
```.py
num1 = int(input())
num2 = int(input())

if num1 % 2 == 1 and num2 % 2 == 1 :
    out = "NO"
    
elif num1 % 2 == 1 or num2 % 2 == 1:
    out = "YES"

else:
    out = "NO"

print(out)
```
![image](https://user-images.githubusercontent.com/89135778/188260218-020a3dbd-063b-4f50-b777-b10ac1ddb99d.png)

## Sign function
For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
Try to use the cascade if-elif-else for it.
```.py
x = int(input())

if x >= 1:
    print(1)

elif x == 0:
    print(0)

else:
    print(-1)
```
![image](https://user-images.githubusercontent.com/89135778/187914094-78572fa7-1a32-4e1f-b66a-fc01131b76a2.png)

## Numbers in ascending order
Given three different integers, print YES if they're given in ascending order, print NO otherwise.
```.py
a = int(input())
b = int(input())
c = int(input())

if a < b and b < c:
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/187915652-f6799554-152e-462b-a197-c846685b23d0.png)

## Is three digit
Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.
```.py
a = int(input())

if a > 99 and a < 1000:
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/187916397-9ce08991-9c4b-4244-bfd2-c719eff10e8d.png)

## Minimum of three numbers
Given three integers, print the smallest value.
```.py
a = int(input())
b = int(input())
c = int(input())

if a<b and a<c:
    print(a)

elif b<c and b<a:
    print(b)

else:
    print(c)
```
![image](https://user-images.githubusercontent.com/89135778/187917133-2b995d14-897b-4e01-8c7b-f2b976314aad.png)

## Equal numbers
Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
```.py
a = int(input())
b = int(input())
c = int(input())

if a==b==c:
    print(3)

elif a==b or b==c or a==c:
    print(2)

else:
    print(0)
```
![image](https://user-images.githubusercontent.com/89135778/187918161-8a6e06ea-4452-4200-8de4-53cca7b2f4ca.png)

## Rook move
```.py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/188260330-22f846e9-83db-4ca8-866a-96c91b515d8c.png)

## Chess board - black square
Given a square of a chessboard. Print BLACK if it's black and print WHITE otherwise.
The program receives two numbers from 1 to 8 each - the column and the row number of the square.
```.py
x = int(input())
y = int(input())

if (x+y) % 2 == 0:
    print("BLACK")

else:
    print("WHITE")
```
![image](https://user-images.githubusercontent.com/89135778/188260885-cf74add2-42c0-4d8a-baea-1fac6f6f0e4e.png)

## Chess board - same color
Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.
```.py

```

## Distance to closest point
Given the coordinates of the three points A, B, and C on a line. Print a distance from the point A to closest point to it.
```.py
a = int(input())
b = int(input())
c = int(input())

ab = abs(a-b)
ac = abs(a-c)

if ab < ac:
    print(ab)
else:
    print(ac)
```
![image](https://user-images.githubusercontent.com/89135778/188311140-30d95924-fe96-4fb1-a9ab-74a24f672c04.png)

## Digits in ascending order
Given a three-digit integer, print YES if its digits go in ascending order, print NO otherwise.
```.py
a = int(input())

cen = a // 100
dec = a // 10 % 10
uni = a % 10

if uni > dec and dec > cen:
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/187920199-bcf79cd3-52c3-47cb-a6ad-d66632a8d779.png)

## Four-digit palindrome
A palindrome is a number which reads the same when read forward as it it does when read backward. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
```.py
a = input()

if a[0] == a[-1] and a[1] == a[-2]:
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/187921887-b185f27f-bc8f-43bd-b6d9-2de66ee08ecd.png)

## King move
Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
```.py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1-x2 < 2 and x1-x2 > -2 and y1-y2 < 2 and y1-y2 > -2: 
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/188261600-edefc1f6-ff87-4767-8d64-9fd76396493e.png)

## Bishop moves
In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.
```.py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1-x2 == y1-y2 or x1-x2 == y2-y1: 
    print("YES")
else:
    print("NO")
```
![image](https://user-images.githubusercontent.com/89135778/188261800-c604ef65-a23e-4808-a299-85b99e563dec.png)

## Queen move
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.
```.py

```

## Index of outlier
Given three integers: two are equal to each other and the third one is different. Print the index number of this different one - 1, 2 or 3.
```.py
a = int(input())
b = int(input())
c = int(input())

if a == b:
    print(3)

elif b == c:
    print(1)

else:
    print(2)
```
![image](https://user-images.githubusercontent.com/89135778/187923597-612c1b95-0b35-4d3c-a5e8-3624b8d4729e.png)

## Knight move
Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.
```.py

```

## Chocolate bar
Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
The program reads three integers: n, m, and k. It should print YES or NO.
```.py

```

## Leap year
Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:

- a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
- a year is always a leap year if its number is exactly divisible by 400
Warning. The words LEAP and COMMON should be printed all caps.
```.py

```

## Days in month
Given a month - an integer from 1 (January) to 12 (December), print the number of days in it in the year 2017 (or any other non-leap year).
```.py

```

## Next day
Given the month (an integer from 1 to 12) and the day in it (an integer from 1 to 31) in the year 2017 (or in any other common year), print the month and the day of the next day to it. The first test corresponds to March 30 and March 31. The second test corresponds to March 31 and April 1.
```.py

```

## Linear equation
Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.
```.py

```

## Vertices of rectangle
Given integer coordinates of three vertices of a rectangle whose sides are parallel to the coordinate axes, find the coordinates of the fourth vertex of the rectangle. In the first test the three given vertices are (1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6).
```.py

```

## Sort three numbers
Given three integers, print them in ascending order.
```.py

```

## White pawn move
A white chess pawn moves up vertically one square at a time. An exception is a pawn on a row #2: it can move either one or two squares up. In addition, a white chess pawn captures diagonally up one square to the left or right. A white chess pawn can never occur on a row #1.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first square, and then the last two - for the second square. The program should print YES if a white pawn can possibly move from the first square to the second square in one move in some game - either by move or by capture. The program should print NO otherwise. The first four tests correspond to the green arrows on the picture below.
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
