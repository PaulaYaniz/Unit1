Create a program that calculates the tax for a salary entered by the user following the table below:

| Tax rate  |  Salary range (US) |
| ------------- | ------------- |
| 5%  | 0 - 10.000 |
| 10%  | 10.001 - 50.000  |
| 15%  | 50.001 - 100.000  |
| 25%  | 100.001 -  |

```.py
if salary >= 0 and salary <= 10000:
    taxes = int(salary * 0.05)

elif salary >= 10001 and salary <= 50000:
    taxes = int(salary * 0.1)

elif salary >= 50001 and salary <= 100000:
    taxes = int(salary * 0.15)

elif salary >= 100001:
    taxes = int(salary * 0.25)

print("You pay", str(taxes)+"$ USD in taxes.")
```

![image](https://user-images.githubusercontent.com/89135778/188128744-5fbaeb32-6554-44d3-b19c-18f9e12f6224.png)
![image](https://user-images.githubusercontent.com/89135778/188129240-3f34e018-f7d7-4e28-97d4-230301b5fa62.png)
![image](https://user-images.githubusercontent.com/89135778/188128618-99b1dcce-dea4-4ec1-b3f6-97ae4429f9aa.png)
