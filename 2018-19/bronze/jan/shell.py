with open('shell.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
steps=[list(map(int,line.split())) for line in lines[1:]]

result=0
#simulate every starting point for the pebble
for i in range(1,4):
    pebble=i
    points=0
    #go through the steps and find how many guesses were correct
    for step in steps:
        if step[0]==pebble:
            pebble=step[1]
        elif step[1]==pebble:
            pebble=step[0]
        if pebble==step[2]:
            points+=1
    result=max(result,points)

with open('shell.out','w') as fout:
    fout.write(str(result)+'\n')
