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
    jug_3 = 0
    steps.append((jug_3, jug_5)) # Empty the 3-Gallon jug

    jug_5, jug_3 = pour(jug_5, jug_3, 3)
    steps.append((jug_3, jug_5)) # Pour the remaining 2 gallons from the 5-gallon jug into the 3-gallon jug

    jug_5 = 5
    steps.append((jug_3, jug_5)) ## Fill the 5 gallon jug again

    jug_5, jug_3 = pour(jug_5, jug_3, 3)
    steps.append((jug_3, jug_5)) # Pour from the 5-gallon jug into the 3-gallon jug until it is full

    return steps


# print the Steps
steps = water_jug_riddle()
for i, (jug_3, jug_5) in enumerate(steps):
    print(f"Step {i + 1}: 3-gallon jug = {jug_3} gallons, 5-gallon jug ={jug_5} gallons")
