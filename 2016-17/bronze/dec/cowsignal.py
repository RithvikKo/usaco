with open('cowsignal.in','r') as fin:
    lines=fin.readlines()

m,n,k=map(int,lines[0].split())
signal=[line.strip() for line in lines[1:]]

result=[]
#multiply each row and the amount of rows by k
for row in signal:
    for i in range(k):
        result.append(''.join([char for char in row for j in range(k)]))

with open('cowsignal.out','w') as fout:
    for row in result:
        fout.write(row+'\n')
