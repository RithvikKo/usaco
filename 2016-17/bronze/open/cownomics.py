with open('cownomics.in','r') as fin:
    lines=fin.readlines()

n,m=map(int,lines[0].split())
spotty=[line.strip() for line in lines[1:n+1]]
plain=[line.strip() for line in lines[n+1:]]

result=0
#iterate through each column
for i in range(m):
    #check if any characters are in both the spotty and plain columns
    spotty_columns=set([genome[i] for genome in spotty])
    plain_columns=set([genome[i] for genome in plain]))
    if len(spotty_columns.intersection(plain_columns))==0:
        result+=1

with open('cownomics.out','w') as fout:
    fout.write(str(result)+'\n')
