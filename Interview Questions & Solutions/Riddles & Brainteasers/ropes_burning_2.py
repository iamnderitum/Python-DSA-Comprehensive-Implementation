class Rope:
    def __init__(self):
        self.burned = False
        self.time_burned = 0

    def burn(self, duration):
        if not self.burned:
            self.time_burned += duration
            if self.time_burned >= 60:
                self.burned = True
                return 60 - (self.time_burned - duration)  # Return remaining time after it burns out
        return duration

    def is_burned_out(self):
        return self.burned

def measure_45_minutes():
    rope1 = Rope()
    rope2 = Rope()
    
    time_elapsed = 0
    
    # Light rope1 from both ends and rope2 from one end
    while not rope1.is_burned_out():
        time_elapsed += rope1.burn(30)  # Rope1 burns out in 30 minutes
    
    # After rope1 burns out, light the other end of rope2
    if rope1.is_burned_out():
        time_elapsed += rope2.burn(15)  # Rope2 burns out in 15 more minutes
    
    return time_elapsed

# Run the simulation
total_time = measure_45_minutes()
print(f"Total time measured: {total_time} minutes")

# Output should be:
# Total time measured: 45 minutes
