#first of all lets know this that string is immutable that means it
#cant be changed but immutable means we cant change the letters or characters in place
#but when we apply method like .upper() or .lower() it copy the string and make a new string and works on that

a = "!!!PriyansHu !!! Priyanshu!!!" #assigning a variable
print(len(a)) #printing the length of the string
print(a.upper()) #uppercase all the characters
print(a.lower())#lowercase all the characters
print(a.rstrip("!")) #remove whatever we write into the bracket inside the colon
print(a.replace("priyanshu","Harry")) #replace is a function which leads to replace the string with another
# string like the first input is the string which needs to be replaced and the second input is which will take place
print(a.split(" ")) #split functions splits the characters in the string into the list
print(a.capitalize()) #it capitalizes the first letter of the word and sets in the lowercase rest


str1 = "Welcome to Console!!!" #another variable
print(len(str1)) #printing the length of string which is 21
print(len(str1.center(50))) #here the length of the first string was 25 then it added the 25 more to fix it to center
print(a.count('!')) #it counts how many times the thing in the quotation is used, and it tells us in the output
print(a.endswith('!')) # it gives answer in the boolean data type like whether it ends with or not
print(str1.find('tos')) #it returns like the index of the letter which is in the quotation very first time when it was use
#and when the word letter not formed it returns -1
print(str1.index('to')) #it is similar to find, but it gives error when not found
print(str1.isalnum()) #tells if alpha-numeric or not
print(str1.isalpha()) #tells if its consist of alphabets or not
print(str1.islower()) #tells that all the words are lower or not if not then returns false
print(str1.isupper()) #tells that all the words are upper or not if not then returns false
print(str1.isnumeric()) #tells that all the words are numerals or not if not then returns false
print(str1.isprintable()) #tells the str is printable or not
print(str1.isspace()) #tells whether it consist white spaces
print(str1.istitle()) #tells whether it is a title or not
print(str1.startswith('W')) #starts with then true or false
print(str1.swapcase()) #swap the lower to upper and vice versa
print(str1.title()) #converts with title 
