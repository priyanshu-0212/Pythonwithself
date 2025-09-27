a = int(input("Enter your age: ")) #taking user input
print("Your age is: ", a) #printing the age of the user
#conditional statement
#conditional operators
# >,< ,<=, >=,==

print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)


#example of a voter or non-voter
if(a>=18 and a<=60):
    print("You can vote")
elif(a<18 or a>60):
    print("You can't vote")



#practice by own
#counting the words
a = "Hello World"
count = 0
for s in a:
    if (s.isalpha()):
        continue
    else:
        count+=1
print(len(a)-count)

#printing the middle element
a = "HelloWorlds"
print(a[int(len(a)/2)])

#sorting the list and printing the max and then printing the max element index
b = [1,2,5,2,7,8]
print(sorted(b))
print(max(b))
print(b.index(max(b)))
