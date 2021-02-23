#flips a rectangle of cows
def flip(cows,x,y):
    for i in range(x+1):
        for j in range(y+1):
            cows[i][j]=not cows[i][j]
    return cows

with open('cowtip.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n=int(lines[0])
cows=[[bool(int(i)) for i in line] for line in lines[1:]]

result=0
#iterate though each row, starting from the last row
for i in range(n-1,-1,-1):
    #iterate though each cow in each row, starting from the last cow
    for j in range(n-1,-1,-1):
        if cows[i][j]:
            cows=flip(cows,i,j)
            result+=1

with open('cowtip.out','w') as fout:
    fout.write(str(result)+'\n')
