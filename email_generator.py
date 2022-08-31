import random

grad = input("What is your graduation year?: ")
name = input("What is your name?: ").lower()
surname = input("What is your surname?: ").lower()
rand = random.randint(1, 9)

print(grad+"."+name+"."+surname+"."+str(rand)+"@uwcisak.jp")
