import math 
import time

def sqrt(n,d):
    time.sleep(d / 1000)
    print(f"Square root of {n} after {d} milliseconds is {math.sqrt(n)}")

n = int(input())
d = int(input())
sqrt(n, d)