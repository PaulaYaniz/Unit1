```.py
max_num_tries = 5

# START NUMBER
start_number = input("Please enter the start number: ")
try:
    int(start_number)
    is_int = True
except ValueError:
    is_int = False
while is_int is not True and max_num_tries > 0:
    max_num_tries -= 1
    start_number = input(f"Error. You have {max_num_tries} chances left. Please enter an integer: ")
    try:
        int(start_number)
        is_int = True
    except ValueError:
        is_int = False

# END NUMBER
if max_num_tries != 0:
    end_number = input("Please enter the end number: ")
    try:
        int(end_number)
        is_int = True
    except ValueError:
        is_int = False
    while is_int is not True and max_num_tries > 0:
        max_num_tries -= 1
        end_number = input(f"Error. You have {max_num_tries} chances left. Please enter an integer: ")
        try:
            int(end_number)
            is_int = True
        except ValueError:
            is_int = False

# STEP NUMBER
    if max_num_tries != 0:
        step_number = input("Please enter the step number: ")
        try:
            int(step_number)
            is_int = True
        except ValueError:
            is_int = False
        while is_int is not True and max_num_tries > 0:
            max_num_tries -= 1
            step_number = input(f"Error. You have {max_num_tries} chances left. Please enter an integer: ")
            try:
                int(step_number)
                is_int = True
            except ValueError:
                is_int = False

# ALL TOGETHER
        if max_num_tries != 0:
            start_number = int(start_number)
            end_number = int(end_number)
            step_number = int(step_number)

            if step_number > 0:
                while start_number <= end_number:
                    print(start_number)
                    start_number += step_number

            if step_number < 0:
                while start_number >= end_number:
                    print(start_number)
                    start_number += step_number
```

![image](https://user-images.githubusercontent.com/89135778/188453771-f72c0c6d-429d-4cbf-81f5-744e610ab96f.png)
![image](https://user-images.githubusercontent.com/89135778/188454327-a41be870-38b0-44ab-b14b-bf791930bf8d.png)
