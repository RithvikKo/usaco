n=int(input())
cows=sorted(list(map(int,input().split())))
containers=sorted(list(map(int,input().split())))
result=1

#iterate through all containers
for container in containers:
    fit=0
    #since tree is symmetrical, we only need to count the number of cows that can fit inside the current container
    for cow in cows:
        if cow<=container:
            fit+=1
    cows=cows[1:]
    result*=fit

print(result)
