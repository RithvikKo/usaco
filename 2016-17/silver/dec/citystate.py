import string

with open(file_name+'.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
cities=[]
states={}
#create a dictionary of states with a list of cities for each state
for line in lines[1:]:
    city,state=line.split()
    city=city[:2]
    #convert strings into numbers
    i,j=string.ascii_uppercase.index(city[0]),string.ascii_uppercase.index(city[1])
    city=i*26+1+j+1
    i,j=string.ascii_uppercase.index(state[0]),string.ascii_uppercase.index(state[1])
    state=i*26+1+j+1
    #don't add cities with the same two letters as their state
    if city!=state:
        cities.append([city,state])
        if state in states:
            states[state].append(city)
        else:
            states[state]=[city]

result=0
#iterate through the cities and check if the city is a state and if the state is in a city in that state
for city,state in cities:
    if city in states and state in states[city]:
        result+=states[city].count(state)

with open(file_name+'.out','w') as fout:
    fout.write(str(result//2)+'\n')
