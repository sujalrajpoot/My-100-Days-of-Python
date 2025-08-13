import pandas  # This is an example of external module
import hashlib  # This is an example of built in module

print("Hi")

# Dont worry about how to use these modules just yet!
csv_data = pandas.read_csv("03-Day3-Modules-and-Pip//one.csv")
m = hashlib.sha256()
print(csv_data, m)