#Check whether a number is divisible by 3, 5, or both.
num = int(input("num =  "))

if(num%3 == 0 or num%5 == 0):
    print("Yes")
else:
    print("No")