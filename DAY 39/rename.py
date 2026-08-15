# for give space in day 1 to 100

import os

for i in range(0,100):
    os.rename(f"Data/Day{i+1}" , f"Data/Day {i+1}")