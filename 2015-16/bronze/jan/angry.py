with open('angry.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
hay_bales=sorted(list(map(int,lines[1:])))

result=0
#iterate through all hay bales and greedily search for the hay bale that results in the most exploded hay bales
for i in range(n):
    hay_bale=hay_bales[i]
    exploded=t=1
    left=right=i
    #go through each time step, keeping track of the leftmost and rightmost exploded hay bales and total exploded hay bales
    while True:
        if left!=None:
            new_left=None
            for j in range(left-1,-1,-1):
                if hay_bales[j]<hay_bales[left]-t:
                    break
                else:
                    new_left=j
                    exploded+=1
            left=new_left
        if right!=None:
            new_right=None
            for j in range(right+1,n):
                if hay_bales[j]>hay_bales[right]+t:
                    break
                else:
                    new_right=j
                    exploded+=1
            right=new_right
        t+=1
        if left==None and right==None:
            break
    result=max(result,exploded)

with open('angry.out','w') as fout:
    fout.write(str(result)+'\n')
