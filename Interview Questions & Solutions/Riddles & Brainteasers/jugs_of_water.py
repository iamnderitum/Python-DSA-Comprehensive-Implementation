"""  Jugs Of Water
    --------------

    Problem Statement
    -----------------
    You have a five gallons jug and a three gallons jug, and an unlimited
    supply of water (but no measuring cups) How Would you come up with exactly
    four gallons of water?

    """
def pour(from_jug, to_jug, to_jug_capacity):
    transfer = min(from_jug, to_jug_capacity - to_jug)
    return from_jug - transfer, to_jug + transfer

def water_jug_riddle():
    # Initialize the Jugs.
    jug_3 = 0
    jug_5 = 0

    # Steps to measure exactly 4 gallons using the jugs
    steps = []

    # Step 1: Fill the 3-gallon jug
    jug_3 = 3
    steps.append((jug_5, jug_3)) # Empty the 3-Gallon jug

    # Step 2: Pour the 3-gallon jug into the 5-gallon jug
    jug_3, jug_5 = pour(jug_3, jug_5, 5)
    steps.append((jug_3, jug_5)) 

    # Step 3: Fill the 3-gallon jug again
    jug_3 = 3
    steps.append((jug_5, jug_3)) 

    # Step 4: Pour water from the 3-gallon jug into the 5-gallon jug until the 5-gallon jug is full
    jug_3, jug_5 = pour(jug_3, jug_5, 5)
    steps.append((jug_5, jug_3)) 

    # Step 5: Empty the 5-gallon jug
    jug_5 = 0
    steps.append((jug_5, jug_3))

    # Step 6: Pour the remaining 1 gallon from the 3-gallon jug into the 5-gallon jug
    jug_3, jug_5 = pour(jug_3, jug_5, 5)
    steps.append((jug_5, jug_3))

    # Step 7: Fill the 3-gallon jug again
    jug_3 = 3
    steps.append((jug_5, jug_3))

    # Step 8: Pour all 3 gallons from the 3-gallon jug into the 5-gallon jug
    jug_3, jug_5 = pour(jug_3, jug_5, 5)
    steps.append((jug_5, jug_3))

    return steps


# print the Steps
steps = water_jug_riddle()
for step in steps:
    print(f"5-gallon jug: {step[0]} gallons, 3-gallon jug: {step[1]} gallons")
