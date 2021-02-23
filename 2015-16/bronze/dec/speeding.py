with open('speeding.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n,m=map(int,lines[0].split())
road_segments=[list(map(int,line.split())) for line in lines[1:n+1]]
driving_segments=[list(map(int,line.split())) for line in lines[n+1:]]

road_segment_miles=road_segments[0][0]
road_segment_index=0
driving_segment_miles=driving_segments[0][0]
driving_segment_index=0
result=max(0,driving_segments[0][1]-road_segments[0][1])
#iterate through each mile and greedily search for the maximum speed over the speed limit
for mile in range(101):
    #update road segment
    if mile>road_segment_miles:
        road_segment_index+=1
        road_segment_miles+=road_segments[road_segment_index][0]
    #update driving segment
    if mile>driving_segment_miles:
        driving_segment_index+=1
        driving_segment_miles+=driving_segments[driving_segment_index][0]
    result=max(result,driving_segments[driving_segment_index][1]-road_segments[road_segment_index][1])

with open('speeding.out','w') as fout:
    fout.write(str(result)+'\n')
