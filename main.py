import time

print("we good?")
print("we good")

with open("testFile.txt", 'w') as f:
    f.write("we good.")

with open("testFile.txt", 'r') as l:
    print(l.readline())

time.sleep(10)

print("we good!")