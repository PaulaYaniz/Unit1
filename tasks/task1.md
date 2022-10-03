# Task 1
## Question 1: 
### What is the most powerful computer? Glad you asked. Watch [this](https://youtu.be/PS_PlorW6pM) video about Sierra Computer. Describe below points that surprised you the most.
What surprised me the most about this video is that the computer takes up a lot of physical space to store. It is 7000 square feet (approx. 650 square meters) big!
I have also seen how the country of the United States of America and its people support technology and like to invest in it. That is good because these kinds of advanced technology need popular support, as they are super powerful. They can do many great things: medical explorations, cancer research, etc. However, they can also do a lot of bad things according to many people’s perspectives, such as nuclear development.

## Question 2: 
### Supercomputers are currently used to investigate solutions to real life problems from cancer research, Ai, economics, or brain simulation. Military uses are also one major force behind the development of these machines. Analyze the benefits and possible drawbacks of developing supercomputers in our modern world? Should we do it?
The drawbacks of developing computers in our modern world is that there will be a moment in which supercomputers will be able to create mega-hiper-supercomputers, and by that moment the humans won't be able to control them and the machines will destroy the world. 
However, supercomputers also do a lot of great things for humanity. They save human lives thanks to their technology (in medical technology, for example).
For that reasons, we should continue developing them but also taking control of them. The moment we lose control over supercomputers, the moment the world will be chaos. 

## Question 3: 
#### Identify the most advanced computer in your Country (What, specs, location, uses). 
The most advanced computer in Spain is MareNostrum, from BSC (Barcelona Supercomputing Center). The computer runs SUSE Linux 11 SP3 Operative System and it occupies 180 square meters. It has 14 PB of storage, a speed of 13.7 PFlops and a power of 1.3 MW.

Among its many uses, those of scientific research, simulations and modeling and weather forecasting stand out.

Bibliography:
http://www.bsc.es/



## Programming task
In a school there are 2400 students and each student uses one locker. Each locker has a unique number from 1 to 2400. The lockers are to be painted in four colors: red, white, yellow and blue, in order of locker numbers, as shown in the following table.link
![image](https://user-images.githubusercontent.com/89135778/190984718-40e31603-486e-47c8-8230-07fdc51d14ee.png)

The pattern of colors continues in this manner. For example, locker number 15 will be painted yellow.


### Task 1: Create a program and the flow diagram that shows the colors of all the lockers from 1 to 2400
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

#### Flowchart:
![CS-QUIZZES-task1-1 drawio](https://user-images.githubusercontent.com/89135778/193600904-c128eed4-ec1e-438d-830d-618f3cd48efc.png)


### Task 2: Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.
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

#### Flowchart:
![CS-QUIZZES-task1-2 drawio](https://user-images.githubusercontent.com/89135778/193600825-7d8ab43b-96ab-487c-a27f-5714e77fdb09.png)
