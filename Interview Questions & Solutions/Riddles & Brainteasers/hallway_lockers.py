"""
            Hallway Lockers
           ----------------

           Problem Statement
           -----------------

You are in a hallway  lined with 100 lockers. You start with one pass and open the 
lockers, so that the opened lockers are now with their doors opened out. You begin
by closing every second locker. Then you go close every third locker and close it if its
closed - we will refer to this as "toggling" the lockers. You continue toggling every
nth locker on pass number n. After  your hundredth pass of the hallway, in which you
toggle only locker number 100,how many lockers are open?
"""

import math

def count_open_lockers(num_lockers):
    open_lockers = set()
    for i in range(1, int(math.sqrt(num_lockers)) + 1):
        open_lockers.add(i * i)
    return len(open_lockers)

# Number of lockers
num_lockers = 100

# Calculate and print the number of open lockers
num_open_lockers = count_open_lockers(num_lockers)
print(f"After 100 passes, {num_open_lockers} locker(s) remain open.")
