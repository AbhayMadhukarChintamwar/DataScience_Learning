
import sys
from time import sleep

sys.setrecursionlimit(11)
print(sys.getrecursionlimit())

count =1

def greet():
    global  count
    print("Hello!", count)
    count += 1
    sleep(0.02)
    greet()

greet()