class Cow:
    def __init__(self,dir,x,y):
        self.north=dir=='N'
        self.x=int(x)
        self.y=int(y)
        self.steps=0
        self.moving=True
        self.stops=[]

	#calculate if cow stops at an intersection
    def intersects(self,intersection):
        if self.north:
            if intersection.x==cow.x and intersection.y>=cow.y:
                return True
        else:
            if intersection.y==cow.y and intersection.x>=cow.x:
                return True
        return False

	#move cow
    def move(self,step):
        if self.moving:
            if self.north:
                self.y+=step
            else:
                self.x+=step
            self.steps+=step

	#determine distance to next stop
    def dist_to_next_stop(self):
        if self.moving:
            return self.stops[0].y-self.y if self.north else self.stops[0].x-self.x
        return False

	#check if cow is at a stop
    def at_stop(self):
        if self.moving:
            return self.moving and self.x==self.stops[0].x and self.y==self.stops[0].y
        return False

class Intersection:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.cross_count=0
        self.eaten=False

def done(cows):
    return not any([cow.moving for cow in cows])

n=int(input())
cows=[input().split() for _ in range(n)]
cows=[Cow(*cow) for cow in cows]

#create intersections
intersections=[Intersection(a.x,b.y) for a in cows for b in cows if a!=b]

filtered=[]
#filter intersections
for intersection in intersections:
    for cow in cows:
        if cow.intersects(intersection):
            filtered.append(intersection)
            break
intersections=filtered

#create stops for each cow
for cow in cows:
    cow.stops=list(filter(lambda i:cow.intersects(i),intersections))

#mark cows with no stops
for cow in cows:
    if len(cow.stops)==0:
        cow.steps='Infinity'
        cow.moving=False

#sort the stops of each cow
for cow in cows:
    if cow.moving:
        if cow.north:
            cow.stops=sorted(cow.stops,key=lambda i:i.y)
        else:
            cow.stops=sorted(cow.stops,key=lambda i:i.x)

#simulate until all cows have stopped or will never stop
while not done(cows):
	#calculate the smallest distance to the next stop and move cows by that amount
    step_size=min([cow.dist_to_next_stop() for cow in cows if cow.moving])
    for cow in cows:
        cow.move(step_size)

    deferred_actions=[]
	#check if each cow is at a stop
    for cow in cows:
        if cow.at_stop():
			#stop cows if the stop is already eaten
            if cow.stops[0].eaten:
                cow.moving=False
            else:
                deferred_actions.append(cow.stops[0])
				#if no more stops then cow will continue forever
                if len(cow.stops)==1:
                    cow.steps='Infinity'
                    cow.moving=False
            del cow.stops[0]

	#mark stops as eaten
    for deferred_action in deferred_actions:
        deferred_action.eaten=True

for cow in cows:
    print(cow.steps)
