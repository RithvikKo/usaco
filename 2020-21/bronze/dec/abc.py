ums=sorted(list(map(int,input().split())))
#a and b are the smallest two numbers
a=nums[0]
b=nums[1]
#a+b+c is the largest number
print(str(a)+' '+str(b)+' '+str(nums[-1]-a-b))
