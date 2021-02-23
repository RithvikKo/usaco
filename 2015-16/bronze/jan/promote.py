with open('promote.in','r') as fin:
    lines=fin.readlines()

promotions=[list(map(int,line.split())) for line in lines]

result=[0,0,0]
#iterate through each division excluding bronze
for i in range(1,4):
    #add number of people before and after for current division and any higher division
    for j in range(i,4):
        result[i-1]+=promotions[j][1]-promotions[j][0]

with open('promote.out','w') as fout:
    for i in result:
        fout.write(str(i)+'\n')
