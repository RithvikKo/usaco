#use dfs to check if src can travel to dst
def dfs(src,dst,belts):
    if src==dst:
        return True
    for belt in belts:
        if belt[0]==src:
            if dfs(belt[1],dst,belts):
                return True
    return False

with open('factory.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
belts=[list(map(int,line.split())) for line in lines[1:]]

result=-1
#iterate through all stations
for i in range(1,n+1):
    done=False
    #check if all stations can travel to current station
    for j in range(1,n+1):
        if j!=i and not dfs(j,i,belts):
            done=True
            break
    if not done:
        result=i
        break

with open('factory.out','w') as fout:
    fout.write(str(result)+'\n')
