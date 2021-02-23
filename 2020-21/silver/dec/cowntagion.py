import math

#dfs through farms and do enough superspreader events to move one cow to each child
def dfs(farm):
    global visited
    global result
    visited[farm-1]=True
    next=[other for other in adjacent[farm] if not visited[other-1]]
    if len(next):
        result+=math.ceil(math.log(len(next)+1,2))
        for other in next:
            dfs(other)
            result+=1

n=int(input())
adjacent={farm:[] for farm in range(1,n+1)}
for _ in range(n-1):
    a,b=map(int,input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)
    
visited=[False]*n
result=0
dfs(1)

print(result)
