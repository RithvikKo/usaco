import itertools

with open('cownomics.in','r') as fin:
    lines=fin.readlines()

n,m=map(int,lines[0].split())
spotty=[line.strip() for line in lines[1:n+1]]
plain=[line.strip() for line in lines[n+1:]]

result=0
#iterate through each set of columns
for combo in itertools.combinations(range(m),3):
    #check if any three characters are in both the spotty and plain columns
    spotty_columns=set([''.join([genome[i] for i in combo]) for genome in spotty])
    plain_columns=set([''.join([genome[i] for i in combo]) for genome in plain])
    if len(spotty_columns.intersection(plain_columns))==0:
        result+=1

with open('cownomics.out','w') as fout:
    fout.write(str(result)+'\n')
