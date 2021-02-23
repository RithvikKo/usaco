#check if point is convered by a rectangle
def point_convered(point,rect):
    if rect[0]<=point[0]<=rect[2] and rect[1]<=point[1]<=rect[3]:
        return True
    return False

with open('billboard.in','r') as fin:
    lines=fin.readlines()

lawnmower=list(map(int,lines[0].split()))
points=[[lawnmower[0],lawnmower[1]],[lawnmower[0],lawnmower[3]],[lawnmower[2],lawnmower[1]],[lawnmower[2],lawnmower[3]]]
cowfeed=list(map(int,lines[1].split()))

points_convered=[]
#find all points that are convered by the cow feed billboard
for point in points:
    if point_convered(point,cowfeed):
        points_convered.append(point)

#determine result based on how many points are covered
result=(lawnmower[2]-lawnmower[0])*(lawnmower[3]-lawnmower[1])
if len(points_convered)==4:
    result=0
elif len(points_convered)==2:
    result-=max(0,min(lawnmower[2],cowfeed[2])-max(lawnmower[0],cowfeed[0]))*max(0,min(lawnmower[3],cowfeed[3])-max(lawnmower[1],cowfeed[1]))

with open('billboard.out','w') as fout:
    fout.write(str(result)+'\n')
