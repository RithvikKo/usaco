with open('word.in','r') as fin:
    lines=fin.readlines()

n,k=map(int,lines[0].split())
essay=lines[1].split()

result=[essay[0]]
line_len=len(essay[0])
#iterate through each word
for word in essay[1:]:
    #start new line if line doesn't fit
    if line_len+len(word)>k:
        result.append(word)
        line_len=len(word)
    #append word to line if it fits
    else:
        result[-1]+=' '+word
        line_len+=len(word)

with open('word.out','w') as fout:
    for line in result:
        fout.write(line+'\n')
