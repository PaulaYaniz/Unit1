 ### Programming task
 In a school there are 2400 students and each student uses one locker. Each locker has a unique number from 1 to 2400. The lockers are to be painted in four colors: red, white, yellow and blue, in order of locker numbers, as shown in the following table.link
![image](https://user-images.githubusercontent.com/89135778/190984718-40e31603-486e-47c8-8230-07fdc51d14ee.png)

The pattern of colors continues in this manner. For example, locker number 15 will be painted yellow.


#### Task 1: Create a program and the flow diagram that shows the colors of all the lockers from 1 to 2400
```.py
# Produce the locker numbers
number_lockers = 2400

# Generate a sequence
for locker in range(1, number_lockers+1, 1):

    # Create a sequence
    color_code = locker % 4
    colors = ["blue", "red", "white", "yellow"]
    color = colors[color_code]

    # Print the results
    print(f"Locker No {locker} is color {color.upper().center(50,'.')}")
```
![image](https://user-images.githubusercontent.com/89135778/190985675-f8767849-1ca2-4fe0-a9a9-acda680f1cef.png)


#### Task 2: Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.
```.py
num = int(input("Please enter a number: "))
# Colors
blue = "\033[1;34;40m"
red = "\033[1;31;40m"
white = "\033[1;37;40m"
yellow = "\033[1;33;40m"

# Saying which color should be each number
if num % 4 == 0:
    col = "blue"
    letters = blue
elif num % 4 == 1:
    col = "red"
    letters = red
elif num % 4 == 2:
    col = "white"
    letters = white
elif num % 4 == 3:
    col = "yellow"
    letters = yellow

# Printing the result
print(f"{letters}Your locker color is {col}")
```
![image](https://user-images.githubusercontent.com/89135778/190985940-8381dd62-4baf-49ba-87ed-33ecbbec7df5.png)
![image](https://user-images.githubusercontent.com/89135778/190986005-aee5011b-54ee-41ae-994d-4fc0135441ad.png)
![image](https://user-images.githubusercontent.com/89135778/190986079-cf786152-8b77-4541-a080-16806d49a018.png)
![image](https://user-images.githubusercontent.com/89135778/190986280-ad7db61b-fffa-4c17-90be-488ef8cd54c8.png)


