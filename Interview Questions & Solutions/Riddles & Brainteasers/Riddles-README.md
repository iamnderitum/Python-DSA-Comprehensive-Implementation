## Riddles & Brainteasers

#### Types
###### 1. Trick Questions 
    - Rely on you having some sort of weird prior knowledge.

    -  Are really the worst type of Riddle and brainteasers one can be asked.
  
    -  Hopefully your're NEVER asked the trick question in an Interview!!!
      They are really UNFAIR Problems to be asked.

    -They are being BANNED at some companies, but you should be aware of them.



###### 1. Estimation Problems
    - You may be required to estimate things that are relevant to your position.
    - Eg: If you're interviewing for the G-mail team at Google you may be asked to estimate
    how much time is spent on Gmail in a given day for an average person or how many people log in to Gmail every day.



###### 2. Math Puzzles.
    - These are puzzles whose background is rooted in some sort of logic or computer science and you should BE ABLE to SOLVE THESE !!!
    - This WILL be the main FOCUS of this Sub-Repository HERENCE NAMED "Riddles & Brainteasers",
    - 
    All Example Code file in above named.



#### Tackling Math Puzzles
    - Dont panic !!! Think and communicate your thoughts.
    - If you are stuck, its recommended to try simplifying the problem
    - Solve it for a small number of items or a special case, and then see if you can generalize it.
    - Remember to check if you can relate the problem to a fundamental data structure or algorithm !!
    - Break down the Problems



### Riddles Examples & Solutions.
#### 1. Bridge-Crossing.
##### Puzzle:
    Four people come to a river in the night. There is a narrow bridge that can only
    hold two people at a time. They have one torch and, because it's night, the torch
    has to be used when crossing the bridge. Person A can cross the bridge in 1 minute
    B in 2 minutes, C in 5 minutes, and D in 10 minutes. When two people cross the
    bridge together, they must move at the slower person's pace.

##### Objective:
    Find the shortest time in which all four people can cross the bridge.

##### Solution Approach:
To solve this puzzle optimally, you need to carefully plan each crossing to minimize the total time.
Below is a step-by-step breakdown of how to achieve this:
###### i. Crossing Strategy:
    - Always send the fastest people back with the torch to maximize their crossing potential.
###### ii. Sequence of Crossings:
    - First, send the two fastest(A & B) across together(2 minutes).
    - A returns with the torch(1 minute).
    - Then, send the two next fastest(C & D) across together(10 Minutes).
    - B returns with the Torch(2 Minutes).
    - Finally, send the two fastest again(A & B) Across together(2 minutes).

###### ii. Total Time Calculation:
    - Sum up the times of all these crossings: 2+1+10+2+2=17

See Code implementation in: **bridge_crossing.py

#### 2. Coins & a Scale
##### Puzzle:
    - You have 8 coins and a two-pan scale. All the coins weigh the same, EXCEPT FOR ONE
    which is heavier than all the others. the coins are otherwise indistunguishable. You
    may make no assumptions about how much heavier the heavy coin is. 

##### Objective:
    - What is the minimum number of weighings needed to be certain of identifying the coin?

##### Solution Approach:
###### i. Divide & Conquer Strategy:
    - Divide the 8 coins in to groups and use the balance scale to elininate groups that cannot contain the heavier Coin.

###### ii. Weighing Strategy:
    - Divide the coins into three groups of 3, 3, and 2 coins.
    - Weigh the two groups of 3 coins against Each Other.
        - If one group is heavier, the heavier coin is in that group.
        - If both groups balance, the heavier coin is in the group of 2 coins.

###### iii. Further Weighings(if needed):
    - Once you identify the group containing the heavier coin, divide that group into 3 & 3.
    - Weigh these two groups agains each other.
        - Again, identify which group contains the heavier coin.

###### iv. Final Weighing:
    - Once you have narrowed down to two coins, Weigh them against each other to identify the heavier one.

##### Minimum Number of Weighings:
    - The minimum number of weighing required to be certain of identifying the heavier coin is 2 weighings.

#### 3. Egg Drop / Two Egg Problem .
    - This is a classic puzzle in computer science and mathematics that involves determining
    the highest floor from which an egg can be dropped without breaking, using the
    minimum number of egg drops.

##### Puzzle:
    - You have two identical eggs and access to a building with "n" floors. One of the 
    floors is the highest floor from which an egg can be dropped without breaking. You
    need to determine this floor using the minimum number of egg drops.

##### Solution Approach:
To solve this problem optimally, you can use a dynamic programming approach to minimize the 
number of drops required. Below is a step-by-step breakdown:

###### i. Define the Problem:
    - let dp(k, n) represent the minimum number of drops required to find the critical floor
      with "k" eggs and "n" floors.

###### ii. Base Cases:
    - If there are no floors(n = 0), no drops are required("dp(k, 0) = 0").
    - If there is only one floor("n = 1"), only one drop is needed("dp(k, 1) = 1").
    - If there is only one egg("k = 1"), you need to drop from each floor one by one("dp(1, n) = n").

###### iii. Recursive Relation
    - for more than one egg and more than one floow, consider dropping the egg from a floor "x":
        * If the egg breaks, you need to check floors below "x" with one less egg
          ('dp(k-1, x-1)').
        * If the egg doesnt break, you need to check floors above 'x' with the same number of eggs
          ('dp(k, n-x)')

    - The worst-case scenario for finding the critical floor is the maximum of these two cases 
      plus one  for the current drop: 'dp(k, n) = 1 + min(max(dp(k-1, x-1), dp(k, n-x)))' 
      for all 'x' from 1 to n.


#### 4. Hallway Lockers
This puzzle involves toggling the state of lockers based on their position in the hallway across multiple passes.

##### Puzzle:
    - You have 100 lockers lined up in a hallway, all initially closed. You begin by
     toggling (opening if closed, closing if open) every second locker (2nd, 4th,
     6th, ...). On the second pass, you toggle every third locker (3rd, 6th, 9th, ...)
     and continue this pattern up to the 100th pass, where you only toggle the 100th
     locker.

    - how many lockers are open?

##### Solution Approach
The key to solving this puzzle lies in understanding the toggling pattern and its effect on the lockers.
Below is how you can approach the solution:
###### i. Initial State:
    - All lockers start closed.

###### ii. Passes and Toggling:
    - On the 'n-th' pass, you toggle every 'n-th' locker. For example:
        * Pass 1: Toggle every 1'st locker(all lockers).
        * Pass 2: Toggle every 2nd locker.
        * pass 3: Toggle every 3rd locker, and so on.

###### iii. Effect Of Toggling:
    - A locker's state changes based on how many times it is toggled. A locker ends up open 
      if it is toggled an odd number of times(Initially closed, then opened and closed repeatedly).

###### iv. Determine Open Lockers:
    - A locker 'k' will be toggled on every pass where 'n' is a divisor of 'k'. Hence, locker 'k'
     will end up open if it has an odd number of divisors(perfect squares have an odd number of
     divisors because one of them is repeated).

###### v. Counting Open Lockers:
    - Lockers that end up open are those whose positions are perfect squares(1, 4, 9, 16...
     , upto 100 ).


#### 5. Jugs of Water
##### Puzzle:
    - You have a five gallons jug and a three gallons jug, and an unlimited
    supply of water (but no measuring cups) How Would you come up with exactly
    four gallons of water?

##### Solution & Approach:
    - The key to solving this puzzle is to use the two jugs to measure and transfer water between them,
  
    - leveraging their different capacities to get the desired measurement.

##### Steps to solve the Puzzle:
###### i. Fill the 3-gallon jug and pour its contents into 5-gallon jug.

###### ii. Fill the 3-gallon jug again and pour water into the 5-gallon jug until its full.
    * After this step, the 3-gallon jug will have exactly 1 gallon of water left(since 5 - 3 = 2
     gallons can be poured into the 5-gallon jug, leaving gallon in the 3-gallon jug )


###### iii. Empty the 5-gallon jug.

###### iv. Pour the remaining 1 gallon from the 3-gallon jug in to the 5-gallon jug.

###### v. Fill the 3-gallon again and pour all 3 gallons into the 5-gallon jug.
    * After this step, the 5-gallon jug will have exactly 4 gallons of water.


#### 6. Light Switches.
##### Riddle:
    - You are in a room with three light switches, each of which controls one of three
     light bulbs in another room. You cannot see the bulbs from where the switches are.
     You can flip the switches any way you want, but you can only enter the room with 
     the bulbs once.
     
     How can you determine which switch controls which bulb?

##### Solution & Approach:
###### i. Label the switches: Let's call the switches A, B & C.

###### ii. Flip switch A on and leave it on for a few minutes. This allows corresponding bulb to heat up

###### iii. After a few minutes, turn switch A off and turn switch B on. Leave switch C off

###### iv. Enter the room with the bulbs:
    - The bulb that is on is controlled by switch B(Since it's the only one currently turned on)
    - Feel the remaining two bulbs. The one that is warm is controlled by switch A (Since it was on long enough to be warm).
    - The bulb that is off & cold is controlled by switch C (Since it was never turned on)


#### 7. Ropes Burning.
##### Riddle:
    You have two ropes. Each rope takes exactly 60 minutes to burn from one end to the
    other. However, they burn at non-uniform rates, meaning that half of a rope might
    take 59 minutes to burn and the other half only 1 minute.
    
    How can you measure exactly 45 minutes using these ropes?

##### Solution & Approach:
###### i. Light the first rope from both ends and the second rope from one end simultaneously

###### ii. When the first rope has completely burned out(30 min), light the other end of the second rope.

###### iii. The second rope will now take 15 minutes to burn completely since it was already burning for 30 min from one end, and lighting the other end makes it  burn twice as fast.

###### iv. The total time elapsed will be 30 minutes + 15 minutes = 45 minutes