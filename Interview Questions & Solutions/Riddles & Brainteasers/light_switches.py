"""
            Light Switches 
            --------------

           Problem Statement
           -----------------
You are in a halfway next to three light switches, all of which are off. Each switch
activates a different incandescent light bulb in the root at the end of the hall. You
cannot see the lights from where the switches are. Your task is to determine which light
corresponds to each switch. However, you may go into the room with the lights only once.
"""

class LightSwitchRiddle:
    def __init__(self):
        self.bulbs = {
            'A': {'state': 'off', 'warm': False},
            'B': {'state': 'off', 'warm': False},
            'C': {'state': 'off', 'warm': False}
        }
        self.room_entered = False

    def flip_switch(self, switch):
        if self.room_entered:
            print("You can't flip switches after entering the room with the bulbs.")
            return
        if self.bulbs[switch]['state'] == 'off':
            self.bulbs[switch]['state'] = 'on'
        else:
            self.bulbs[switch]['state'] = 'off'

    def wait(self):
        for switch, bulb in self.bulbs.items():
            if bulb['state'] == 'on':
                bulb['warm'] = True

    def enter_room(self):
        self.room_entered = True
        states = {switch: self.bulbs[switch]['state'] for switch in self.bulbs}
        warmth = {switch: self.bulbs[switch]['warm'] for switch in self.bulbs}
        return states, warmth

# Simulation
riddle = LightSwitchRiddle()

# Step-by-step solution
riddle.flip_switch('A')  # Turn switch A on
riddle.wait()  # Wait to let the bulb warm up
riddle.flip_switch('A')  # Turn switch A off
riddle.flip_switch('B')  # Turn switch B on

# Enter the room and check the states and warmth
states, warmth = riddle.enter_room()

# Determine which switch controls which bulb
for switch in 'ABC':
    if states[switch] == 'on':
        print(f"Switch {switch} controls the bulb that is ON.")
    elif warmth[switch]:
        print(f"Switch {switch} controls the bulb that is OFF but WARM.")
    else:
        print(f"Switch {switch} controls the bulb that is OFF and COLD.")

# Output should be:
# Switch B controls the bulb that is ON.
# Switch A controls the bulb that is OFF but WARM.
# Switch C controls the bulb that is OFF and COLD.
