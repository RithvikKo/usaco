import itertools

with open('lineup.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
constraints=[[line.split()[0],line.split()[-1]] for line in lines[1:]]

#initialize cows alphabetically
cows=['Beatrice','Belinda','Bella','Bessie','Betsy','Blue','Buttercup','Sue']
#iterate through all permuations
for permutation in itertools.permutations(cows):
    satisfies=True
    #cows must be next to each other to satify constraints
    for a,b in constraints:
        if abs(permutation.index(a)-permutation.index(b))>1:
            satisfies=False
            break
    if satisfies:
        break

with open('lineup.out','w') as fout:
    for cow in permutation:
        fout.write(cow+'\n')
