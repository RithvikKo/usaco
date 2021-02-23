with open('hoofball.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
cows=sorted(list(map(int,lines[1].split())))

passes=[]
#find what cow each cow passes to
for i in range(n):
    if i is 0:
        passes.append(cows[1])
    elif i is n-1:
        passes.append(cows[-2])
    elif cows[i]-cows[i-1]>cows[i+1]-cows[i]:
        passes.append(cows[i+1])
    else:
        passes.append(cows[i-1])

result=0
for cow in cows:
    if cow not in passes:
        result+=1
#find pairs of cows that pass to each other but don't get passes from anyone else
for i in range(n):
    if passes[cows.index(passes[i])]==cows[i] and passes.count(cows[i])==1 and passes.count(passes[i])==1:
        result+=0.5

with open('hoofball.out','w') as fout:
    fout.write(str(int(result))+'\n')
