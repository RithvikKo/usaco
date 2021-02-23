n=int(input())
flowers=list(map(float,input().split()))

result=0
#iterate through all photos
for i in range(n):
    for j in range(i,n):
		#check if an average flower is in the photo
        if sum(flowers[i:j+1])/(j+1-i) in flowers[i:j+1]:
            result+=1
            
print(result)
