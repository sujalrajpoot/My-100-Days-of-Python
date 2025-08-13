import os

if(not os.path.exists("data")):
    os.mkdir("46-Day-46-os-Module/data")

for i in range(0, 100):
    os.mkdir(f"46-Day-46-os-Module/data/Day {i+1}")