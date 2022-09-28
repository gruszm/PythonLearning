import time
import os

global file
fileName = str("Intermediate/Files/file.txt")

# Open file in read-mode
try:
    file = open(fileName, "rt")
except:
    print("Could not open file")

print(file.read())
print()
file.seek(0)
print(file.read(5))

file.close()

# Open file in write-mode
try:
    file = open(fileName, "at")
except:
    print("Could not open file")

file.write("\nAnd my name is Luigi")
file.close()

# Open file in read-mode
try:
    file = open(fileName, "rt")
except:
    print("Could not open file")

fileContent = file.read()

file.close()

if os.path.exists(fileName):
    os.remove(fileName)

time.sleep(3)

file = open(fileName, "x")
file = open(fileName, "w")
file.write(fileContent)
file.close()