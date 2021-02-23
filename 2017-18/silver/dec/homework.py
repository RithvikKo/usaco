import copy

with open('homework.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n=int(lines[0])
scores=list(map(int,lines[1].split()))

uneaten=scores[-1]
uneaten_len=0
worst=scores[-1]
results=[]
highest=0
#iterate through the scores backward, keeping track of the sum, length, and worst score of the uneaten scores
for i,score in enumerate(scores[n-2:0:-1]):
    uneaten+=score
    uneaten_len+=1
    worst=min(worst,score)
    average=(uneaten-worst)/uneaten_len
    if average>highest:
        highest=average
        results=[n-i-2]
    elif average==highest:
        results.append(n-i-2)

with open('homework.out','w') as fout:
    for result in reversed(results):
        fout.write(str(result)+'\n')
