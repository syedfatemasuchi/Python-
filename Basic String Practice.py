#Take a string as input and print it
str = input("str :  ")
str1 = input("str1 : ")
#Find the length of a string.
print(len(str))
#Print the first and last character of a string.
print(str[0])
print(str[-1])
#Convert a string to uppercase.
print(str.upper())
#Convert a string to lowercase.
print(str.lower)
#Concatenate two strings.
print("str"+"str1")
#Replace a word/character in a string.
print(str.replace('syed','fatema'))
#Reverse a string.
print(str[::-1])
#Count woed in a string.
word = str.split()
print(len(word))
#Find the frequency of a character in a string.
print(str.count("a"))
#Check whether a string is a palindrome
if(str == str[::-1]):
    print("Palindrom")
else:
    print("Not Palindrom")
