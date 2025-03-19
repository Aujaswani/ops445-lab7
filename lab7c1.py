#!/usr/bin/env python3
# Student ID: [seneca_id]
from lab7c import *

t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)
td = Time(0, 50, 0)

# Now you can add them directly with '+'
tsum1 = t1 + td
tsum2 = t2 + td
tsum3 = t3 + td

# Print directly; __str__() will format them
print(f"{t1} + {td} --> {tsum1}")
print(f"{t2} + {td} --> {tsum2}")
print(f"{t3} + {td} --> {tsum3}")
