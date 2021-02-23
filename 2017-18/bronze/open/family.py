#find the mother of the given cow
def mother(cow):
    for relationship in relationships:
        if relationship[1]==cow:
            return relationship[0]
    return None

#calculate how many generations the ancestor is removed from the given cow
def ancestor(ancestor,cow):
    generations=0
    while cow!=None:
        if ancestor==cow:
            return generations
        cow=mother(cow)
        generations+=1
    return None

with open('family.in','r') as fin:
    lines=fin.readlines()

n,bessie,elsie=lines[0].split()
n=int(n)
relationships=[line.split() for line in lines[1:]]

cow=bessie
x=0
#find the common ancestor of Bessie and Elsie and how many generations their common ancestor is removed from them
while cow!=None:
    if ancestor(cow,elsie)!=None:
        break
    cow=mother(cow)
    x+=1
y=ancestor(cow,elsie)

with open('family.out','w') as fout:
    if cow==None:
        fout.write('NOT RELATED\n')
    else:
        if x>y:
            x,y=y,x
            bessie,elsie=elsie,bessie
        if x==0:
            if y==1:
                fout.write(bessie+' is the mother of '+elsie+'\n')
            else:
                greats='great-'*(y-2)
                fout.write(bessie+' is the '+greats+'grand-mother of '+elsie+'\n')
        elif x==1:
            if y==1:
                fout.write('SIBLINGS\n')
            else:
                greats='great-'*(y-2)
                fout.write(bessie+' is the '+greats+'aunt of '+elsie+'\n')
        else:
            fout.write('COUSINS\n')
