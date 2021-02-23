with open('notlast.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
entries=[[line.split()[0],int(line.split()[1])] for line in lines[1:]]

cows={'Bessie':0,'Elsie':0,'Daisy':0,'Gertie':0,'Annabelle':0,'Maggie':0,'Henrietta':0}
#count how much milk each cow produced
for entry in entries:
    cows[entry[0]]+=entry[1]

with open('notlast.out','w') as fout:
    milk=set(cows.values())
    #all cows produced the same amount of milk
    if len(milk)==1:
        fout.write('Tie\n')
    else:
        second=sorted(milk)[1]
        if list(cows.values()).count(second)>1:
            fout.write('Tie\n')
        else:
            for cow,milk in cows.items():
                if milk is second:
                    fout.write(str(cow)+'\n')
