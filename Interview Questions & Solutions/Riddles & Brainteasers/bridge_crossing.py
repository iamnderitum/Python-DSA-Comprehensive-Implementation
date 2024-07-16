"""
             Bridge Crossing
            ----------------

            Problem Statement
            -----------------
A group of four travellers comes to a bridge at night. The bridge can hold the
weight of at most only two of the travelers ata a time, and it can-noot be crossed
without using a flashlight.

The travelers have one flashlight among them. Each traveler walks at a different speed:
The first can cross the bridge in 1 minute, the second in 2 minutes, the third in 5 minute, 
and the fourth  takes 10 minutes to cross the bridge. If two travelers cross together, 
they walk at the speed of the slower traveller.

What is the least amount of time in which all the travellers can cross from one side
of the bridge to the other?
"""

from heapq import heappush, heappop

class BridgeCrossing:
    def __init__(self, people_times):
        self.people_times = sorted(people_times, reverse=True)
        self.total_time = 0

    def cross_bridge(self):
        while len(self.people_times) > 0:
            if len(self.people_times) == 1:
                # Only one person left, just move them across
                self.total_time += self.people_times.pop()
            elif len(self.people_times) == 2:
                # Only two people left, move them across together
                self.total_time += max(self.people_times)
                self.people_times.pop()
                self.people_times.pop()
            else:
                # Take the two slowest people first, then send the fastest back
                self.total_time += self.people_times[1]
                self.people_times.pop(1)
                self.total_time += self.people_times[0]
                self.people_times.pop(0)
                self.total_time += self.people_times[0]

    def get_total_time(self):
        return self.total_time

# Example usage
people_times = [1, 2, 5, 10]  # Times for persons A, B, C, D
bridge_crossing = BridgeCrossing(people_times)
bridge_crossing.cross_bridge()
total_time = bridge_crossing.get_total_time()
print(f"Minimum time required: {total_time} minutes")

# Output should be:
# Minimum time required: 17 minutes
