with open('measurement.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
measurements=sorted([[int(line.split()[0]),line.split()[1],int(line.split()[2])] for line in lines[1:]])
cows={'Bessie':7,'Elsie':7,'Mildred':7}

result=0
leaders=[]
#iterate through all measurements and update milk outputs
for measurement in measurements:
    cows[measurement[1]]+=measurement[2]
    highest_output=max(cows.values())
    new_leaders=[]
    #find new leaders
    for cow,output in cows.items():
        if output==highest_output:
            new_leaders.append(cow)
    if leaders!=new_leaders:
        result+=1
        leaders=new_leaders

with open('measurement.out','w') as fout:
    fout.write(str(result)+'\n')
