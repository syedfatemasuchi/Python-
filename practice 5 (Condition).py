#Check whether a character is a vowel, consonant, digit, or special character.
#Method 1
ch = input("ch  : ")

if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch== "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U"):
    print ("vowel")
elif(ch>"a" and ch<"z" or ch>"A" and ch<"Z"):
     print("Consonant")
elif(ch>='0' and ch<='9'):
     print("Digit")
else:
 print("special character")

 #Method 2
ch = input("ch  : ")
 
if ch in ("aeiou" or "AEIOU"):
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")