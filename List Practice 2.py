list = [1 ,2 ,2 ,1]
copy_list = list.copy()
copy_list.reverse()

if(list == copy_list):
    print("Palindrom")
else:
    print("Not Palindrom")