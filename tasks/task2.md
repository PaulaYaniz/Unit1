## EV Calculator

#### Data (charging_log.csv):
```.csv
date,charge,duration
12.9.22,8.878kWh,12:32:36
15.9.22,3.533kWh,5:02:23
17.9.22,6.828kWh,9:41:46
18.9.22,5.425kWh,7:43:35
```

#### my_lib library
```.py
colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;34m"]
end_code = "\033[00m"
bold_green = "\33[1;32m"

def validate_int_input(msg:str)->int:
    """This function validates that the user enters an integer"""
    end_code = "\033[00m"
    red = "\033[0;31m"
    number = input(msg)
    while not number.isdigit():
        number = input(f"{red}{msg}{end_code}")

    return int(number)
```

#### Introductory menu and options
```.py
from my_lib import validate_int_input, end_code, colors, bold_green
import datetime

welcome_msg = "Welcome to the EV calculator".center(50, "=")
prompt_msg = "Please enter an option [1-4]: "
print(f"{colors[2]}{welcome_msg}{end_code}")
print("Options".center(50))

menu = """1. Average time per kWh
2. Total kWh used
3. Total charge time
4. Show all data
"""
print(menu)
option = validate_int_input(prompt_msg)
while option > 4 or option < 1:
    option = validate_int_input(f"{colors[1]}Invalid option. {prompt_msg}{end_code}")
```
![image](https://user-images.githubusercontent.com/89135778/191210464-fe4eb3e7-282c-42fc-a83a-6007f745906a.png)
![image](https://user-images.githubusercontent.com/89135778/191210606-cbe14982-0dd8-4ceb-9e29-e41aa687d530.png)

#### 1. Average time per kWh
```.py
# Option 1: Average time per kWh
if option == 1:
    index = 0
    total_energy = 0
    all_times = []

    for log in ev_logs:
        if index > 0:
            values = log.split(",")
            date = values[0]
            energy = values[1]
            time = values[2][0:8]
            total_energy += float(energy[0:5])
            all_times.append(time)
        index += 1
    total_time = datetime.timedelta()
    for i in all_times:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        total_time += d
    total_seconds = total_time.total_seconds()
    total_hours = total_seconds/3600
    average_time = total_hours / total_energy
    print(f"{colors[2]}The average time per kWh is {average_time} hours per kWh.")
```
![image](https://user-images.githubusercontent.com/89135778/191210878-21284434-1a7e-4940-87b5-198a4f93ba71.png)

#### 2. Total kWh used
```.py
# Option 2: Calculate total energy
if option == 2:
    index = 0
    total_energy = 0
    for log in ev_logs:
        if index > 0:
            values = log.split(",")
            date = values[0]
            energy = values[1]
            time = values[2]
            total_energy += float(energy[0:5])
        index += 1
    print(f"{colors[2]}The total energy charged is {total_energy}kWh")
```
![image](https://user-images.githubusercontent.com/89135778/191211157-689bd83a-af22-4960-a1cb-8294f0331800.png)

#### 3. Total charge time
```.py
# Option 3: Total charge time
if option == 3:
    index = 0
    all_times = []

    for log in ev_logs:
        if index > 0:
            values = log.split(",")
            date = values[0]
            energy = values[1]
            time = values[2][0:8]
            all_times.append(time)
        index += 1
    total_time = datetime.timedelta()
    for i in all_times:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        total_time += d
    print(f"{colors[2]}The total charge time is {total_time} hours.")
```
![image](https://user-images.githubusercontent.com/89135778/191211285-4563cfbb-ad39-4b8a-b3f4-346ed65d7a94.png)

#### 4. Show all data
```.py
# Option 4: Show all data
with open("charging_log.csv", "r") as file:
    ev_logs = file.readlines()

if option == 4:
    print(f"{bold_green}4. Showing all data{end_code}")
    index = 0
    for log in ev_logs:
        if index > 0:
            # print(log.strip())  # strip removes the \n at the end of the line
            print(f"No.{index}: {log}", end="")
        index += 1
```
![image](https://user-images.githubusercontent.com/89135778/191211571-6f3e8bdc-4f79-4d56-a7c5-66973da16df2.png)
