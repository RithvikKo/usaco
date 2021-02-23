import string

with open('circlecross.in','r') as fin:
    lines=fin.readlines()

points=lines[0].strip()

result=0
#iterate through every cow's enter and exit points
for cow in string.ascii_uppercase:
    once=set()
    #iterate from the enter point to the exit point and find the number of cows with an enter or exit point but not both 
    for point in points[points.index(cow)+1:]:
        if point==cow:
            break
        else:
            if point in once:
                once.remove(point)
            else:
                once.add(point)
    result+=len(once)

with open('circlecross.out','w') as fout:
    fout.write(str(result//2)+'\n')
