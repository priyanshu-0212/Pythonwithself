#for loop in strings
for i in range(10): #initiating for loop
    print(i+1, end=" ")

print("\n") #line changes with this


name = "Priyanshu"
for i in name:
    print(i, end=" ")
    if(i == "a"):
        print("Yes its special")

#for loop in list

colors = ["Red", "Green", "Blue", "Yellow", "Magenta", "Cyan"]
for color in colors:
    print(color, end=", ")
