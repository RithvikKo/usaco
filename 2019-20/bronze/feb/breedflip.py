with open('breedflip.in','r') as fin:
    lines=fin.readlines()

n,a,b=int(lines[0]),lines[1],lines[2]

result=0
last=False
#iterate through a and b
for i in range(n):
    #flip once for each substring of cows
    if a[i]!=b[i] and not last:
        last=True
        result+=1
    else:
        last=False

with open('breedflip.out','w') as fout:
    fout.write(str(result)+'\n')
