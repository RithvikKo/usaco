import copy

#calculates the bounds of a color
def _bounds(color):
    top=left=n
    bottom=right=0
    for i in range(n):
        for j in range(n):
            if canvas[i][j]==color:
                top=min(top,i)
                left=min(left,j)
                bottom=max(bottom,i)
                right=max(right,j)
    return left,bottom,right,top

#checks if a overlaps b
def overlap(a,b):
    bounds=_bounds(b)
    for i in range(bounds[3],bounds[1]+1):
        for j in range(bounds[0],bounds[2]+1):
            if canvas[i][j]==a:
                return True
    return False

with open('art.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
canvas=[[int(i) for i in line.strip()] for line in lines[1:]]
colors=set(cell for row in canvas for cell in row if cell!=0)

result=len(colors)
#iterate though all colors
for a in colors:
    #check if a overlaps any other colors
    for b in colors:
        if a!=b and overlap(a,b):
            result-=1
            break

with open('art.out','w') as fout:
    fout.write(str(result)+'\n')
