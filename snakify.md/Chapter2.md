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

## -- Two digits
Given a two-digit number, print its digits separately.
```.py
a = int(input())

dec = a // 10
uni = a % 10

print(dec, uni)
```
![image](https://user-images.githubusercontent.com/89135778/187663483-ebf40739-8e38-47e9-abfd-316602bd6ed5.png)

## -- Swap digits
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

## -- Last two digits
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

## -- Reverse three digits
Given a three-digit integer number, print its digits in a reversed order.
```.py
a = int(input())

cen = a // 100
dec = a // 10 % 10
uni = a % 10

print(str(uni)+str(dec)+str(cen))
```
![image](https://user-images.githubusercontent.com/89135778/187665382-66cc8ff7-aced-49a5-8bea-697975023c02.png)

## -- Merge two numbers
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

## -- Cyclic rotation
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

## 
```.py

```
