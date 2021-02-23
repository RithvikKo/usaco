with open('moobuzz.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n=int(lines[0])

count=1
i=int(n-.1)//8*15+1
stop=n%8 if stop==0 else stop=8
#check where in the pattern n is
while count<stop:
    i+=1
    if i%3!=0 and i%5!=0 and i%15!=0:
        count+=1

with open('moobuzz.out','w') as fout:
    fout.write(str(i)+'\n')
