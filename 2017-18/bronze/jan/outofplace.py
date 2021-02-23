with open('outofplace.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
heights=[int(line) for line in lines[1:]]
#sort heights
sorted_heights=sorted(heights)

result=-1
#iterate through heights and sorted heights
for i in range(len(heights)):
    #swap every time the heights in both lists are different
    if heights[i]!=sorted_heights[i]:
        result+=1

with open('outofplace.out','w') as fout:
    fout.write(str(max(0,result))+'\n')
