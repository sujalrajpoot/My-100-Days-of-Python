import os 
folders = os.listdir("46-Day-46-os-Module/data")

print(os.getcwd())
# os.chdir("C:/Users")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"46-Day-46-os-Module/data/{folder}"))