## Slices
You are given a string.

In the first line, print the third character of this string.

In the second line, print the second to last character of this string.

In the third line, print the first five characters of this string.

In the fourth line, print all but the last two characters of this string.

In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).

In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).

In the seventh line, print all the characters of the string in reverse order.

In the eighth line, print every second character of the string in reverse order, starting from the last one.

In the ninth line, print the length of the given string.
```.py
S = input()

print(S[2])
print(S[-2])
print(S[:5])
print(S[:-2])
print(S[0::2])
print(S[1::2])
print(S[::-1])
print(S[::-2])
print(len(S))
```
![image](https://user-images.githubusercontent.com/89135778/191235724-9448e8cf-22af-4cd0-b8b0-f6f455ce1257.png)

## The number of words
Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count.
```.py
string = input()
words = string.count(' ') + 1

print(words)
```
![image](https://user-images.githubusercontent.com/89135778/191236180-df5002ce-0c49-4fc2-96a9-a3598ef31931.png)

## The two halves
Given a string. Cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string, so that the first string contains one more characther than the second). Now print a new string on a single row with the first and second halfs interchanged (second half first and the first half second)
Don't use the statement if in this task.
```.py
from math import ceil

string = input()
letters = string.count('') - 1
half = ceil(letters / 2)

first_half = (string[half:])
second_half = (string[:half])

print(first_half + second_half)
```
![image](https://user-images.githubusercontent.com/89135778/191237004-11b62d2d-e3ba-4c4d-bc2e-5996a5776475.png)

## To swap the two words
Given a string consisting of exactly two words separated by a space. Print a new string with the first and second word positions swapped (the second word is printed first).
This task should not use loops and if.
```.py
string = input()

separation = string.find(' ')

word = int(separation)

first_word = (string[:word])
second_word = (string[word::])

print(second_word, first_word)
```
![image](https://user-images.githubusercontent.com/89135778/191237977-4db39e65-0789-484e-a68d-5359d6a7ba36.png)

## The first and last occurrence
Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. If the letter f occurs only once, then output its index. If the letter f does not occur, then do not print anything.
Don't use loops in this task.
```.py
string = input()
a = string.find('f')
b = string.rfind('f')

if a >= 0:
    print(a)
    if a != b:
        print(b)
```
![image](https://user-images.githubusercontent.com/89135778/191241128-b59db735-1252-4e1d-a8c4-d719eb04ae22.png)

## The second occurrence
Given a string that may or may not contain the letter of interest. Print the index location of the second occurrence of the letter f. If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2.
```.py
string = input()
a = string.find('f')
b = string.find('f', a+1)

if a == -1:
    print(-2)
else:
    print(b)
```
![image](https://user-images.githubusercontent.com/89135778/191241367-10a875c8-7071-40db-b4fb-a4df0344b22b.png)

## Remove the fragment
Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them.
```.py
string = input()

first_h = string.find('h')
last_h = string.rfind('h') + 1

between_h = string[first_h:last_h]

print(string.replace(between_h,''))
```
![image](https://user-images.githubusercontent.com/89135778/191242055-18d070fa-3f37-419e-abfa-dffb385b89bf.png)

## Reverse the fragment
Given a string in which the letter h occurs at least two times, reverse the sequence of characters enclosed between the first and last appearances.
```.py
string = input()

first_h = string.find('h')
last_h = string.rfind('h') + 1

between_h = string[first_h:last_h]
between_h_contrary = (between_h[::-1])

until_h = string[0:first_h]
from_h = string[last_h::]

print(until_h+between_h_contrary+from_h)
```
![image](https://user-images.githubusercontent.com/89135778/191242935-0b448bc6-a26a-416b-84e1-a300346fabcc.png)

## Replace the substring
Given a string. Replace in this string all the numbers 1 by the word one.
```.py
string = input()

print(string.replace('1', 'one'))
```
![image](https://user-images.githubusercontent.com/89135778/191244126-a1f8ba5a-7db7-41cc-abbc-ca547305b06c.png)

## Delete a character
Given a string. Remove from this string all the characters @.
```.py
string = input()

print(string.replace('@', ''))
```
![image](https://user-images.githubusercontent.com/89135778/191243960-b6c9add3-4c0c-4b2e-9e79-215f2f6f4fe4.png)

## Replace within the fragment
Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.
```.py
string = input()
first_h = string.find('h') + 1
last_h = string.rfind('h')

part1 = string[0:first_h]
part2 = string[first_h:last_h].replace('h', 'H')
part3 = string[last_h::]

print(part1 + part2 + part3)
```
![image](https://user-images.githubusercontent.com/89135778/191243495-19955d63-701f-4688-b9cb-f0a95483c379.png)

## Delete every third character
Given a string. Delete from it all the characters whose indices are divisible by 3.
```.py
string = input()

result = ''

for i in range(0, len(string)):
    a = string[i]
    if i % 3 != 0:
        result += a

print(result)
```
![image](https://user-images.githubusercontent.com/89135778/191243809-6255363c-18bb-4526-a483-73a6faa1013f.png)
