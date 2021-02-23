with open('whereami.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
mailboxes=lines[1]

#iterate through all sequence lengths
for k in range(1,n+1):
    unique=True
    #iterate through all sequences
    for i in range(n-k):
        #cannot determine location if any sequence is not unique
        if mailboxes.count(mailboxes[i:i+k])>1:
            unique=False
            break
    if unique:
        break

with open('whereami.out','w') as fout:
    fout.write(str(k)+'\n')
