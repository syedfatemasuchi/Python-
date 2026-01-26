#Search for a number x in this tuple using loop
nums= (1,4,9,16,25,36,49,64,81,1000)
x=81
idx=0
while(idx<len(nums)):
    if(nums[idx]==x):
        print("found",idx)
    idx+=1






