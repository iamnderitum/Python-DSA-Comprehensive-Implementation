"""
             Egg Drop
            --------------

           Problem Statement
           -----------------
A tower has 100 floors. You've been given two eggs. The eggs are strong enough that they
can be dropped from a particular floor in the tower without breaking. You been tasked to 
find the highest floor an egg can be dropped without breaking, in as few drops as
possible. If an egg is dropped from above its target floor,it will break. If it is
dropped from that floor  or below, it will be itact and you can test drop the egg
again on another floow.

Show algorithmically how you would go about this in as few drops as possible.
(Your answer should be a number  of the fewest drops needed for testing 2 eggs
on 100 flors)
"""

def eggDrop(n):
    # Initialize a 2D table to store results of subproblems
    dp = [[0 for x in range(n+1)] for y in range(3)]
    
    # Base cases
    for i in range(1, 3):
        dp[i][0] = 0    # Zero floors require zero trials
        dp[i][1] = 1    # One floor requires one trial

    for j in range(1, n+1):
        dp[1][j] = j    # One egg, j floors require j trials

    # Fill the rest of the entries in table using optimal substructure property
    for i in range(2, 3):
        for j in range(2, n+1):
            dp[i][j] = float('inf')
            for x in range(1, j+1):
                res = 1 + max(dp[i-1][x-1], dp[i][j-x])
                if res < dp[i][j]:
                    dp[i][j] = res

    # dp[2][n] will have the result
    return dp[2][n]

# Example usage
n = 100  # Number of floors
minDrops = eggDrop(n)
print(f"Minimum number of drops required in worst case with {n} floors and 2 eggs: {minDrops}")

# Output should be:
# Minimum number of drops required in worst case with 100 floors and 2 eggs: 14
