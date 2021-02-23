with open('badmilk.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n,m,d,s=map(int,lines[0].split())
drink_times=[list(map(int,line.split())) for line in lines[1:d+1]]
sick_times=[list(map(int,line.split())) for line in lines[d+1:]]

possible_bad_milks=[]
not_sick=list(range(1,n+1))
#iterate through all people that got sick and find the milks that all sick people drank
for sick_time in sick_times:
    milks_drank=[drink_time[1] for drink_time in drink_times if drink_time[0]==sick_time[0] and drink_time[2]<sick_time[1]]
    possible_bad_milks.append((set(milks_drank)))
    not_sick.remove(sick_time[0])
possible_bad_milks=set.intersection(*possible_bad_milks)

result=s
#find all people who drank a possible bad milk
for person in not_sick:
    for drink_time in drink_times:
        if drink_time[0]==person and drink_time[1] in possible_bad_milks:
            result+=1
            break

with open('badmilk.out','w') as fout:
    fout.write(str(result)+'\n')
