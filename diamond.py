height = int(input("Enter the height of a diamond: "))

for i in range(height):
    print(" "*(height-i), end="")
    for j in range(1,i+2):
        print("*",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()
for i in range(height-2, -1, -1):
    print(" "*(height-i), end="")
    for j in range(1,i+2):
        print("*",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()