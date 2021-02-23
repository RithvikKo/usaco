import itertools

with open('hps.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
games=[list(map(int,line.split())) for line in lines[1:]]

result=0
permutations=itertools.permutations([1,2,3])
#iterate through all possible assigments of the gestures
for permutation in permutations:
    temp=[[permutation[game[0]-1],permutation[game[1]-1]] for game in games]
    won=0
    for game in temp:
        if (game[0]==1 and game[1]==3) or (game[0]==2 and game[1]==1) or (game[0]==3 and game[1]==2):
            won+=1
    result=max(result,won)

with open('hps.out','w') as fout:
    fout.write(str(result)+'\n')
