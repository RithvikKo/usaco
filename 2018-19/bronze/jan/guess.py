with open('guess.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
animals=[line.split() for line in lines[1:]]

result=0
#iterate through all animals
for animal in animals:
    yeses=0
    #iterate through all other animals and find animal that has the most shared characteristics
    for other in animals:
        if other!=animal:
            animal_characteristics=set(animal[2:])
            other_characteristics=set(other[2:])
            yeses=max(yeses,len(animal_characteristics.intersection(other_characteristics))+1)
    result=max(result,yeses)

with open('guess.out','w') as fout:
    fout.write(str(result)+'\n')
