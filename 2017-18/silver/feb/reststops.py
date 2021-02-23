with open('reststops.in','r') as fin:
    lines=fin.readlines()

l,n,rf,rb=map(int,lines[0].split())
#sort stops by distance
stops=sorted([list(map(int,line.split())) for line in lines[1:]],key=lambda s:s[0])

result=td=0
while True:
    if len(stops)==0:
        break
    best=stops[0]
    best_i=0
    #find the stop with the tastiest grass
    for i,stop in enumerate(stops[1:]):
        if stop[1]>best[1]:
            best=stop
            best_i=i+1
    #remove stops before
    stops=stops[best_i+1:]
    d=best[0]-td
    td=best[0]
    result+=(rf*d-rb*d)*best[1]

with open('reststops.out','w') as fout:
    fout.write(str(result)+'\n')
