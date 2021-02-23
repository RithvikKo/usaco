import itertools

with open('bcs.in','r') as fin:
    lines=fin.readlines()

lines=[line.strip() for line in lines]
n,k=map(int,lines[0].split())
original=[line for line in lines[1:n+1]]
original_size=len([char for row in original for char in row if char is '#'])
pieces=[[line for line in lines[i*n+1:i*n+n+1]] for i in range(1,k+1)]

#mark pieces that have an equal number or more characters than the original figurine
for i,piece in enumerate(pieces):
    if len([char for row in piece for char in row if char is '#'])>=original_size:
        pieces[i]=None

found=False
combos_indexes=itertools.combinations(range(k),2)
#iterate through every combination of pieces, ignoring marked pieces
for combo_indexes in combos_indexes:
    combo=[pieces[combo_indexes[0]],pieces[combo_indexes[1]]]
    if combo[0]!=None and combo[1]!=None:
        #try shifting in all four directions
        for a in range(n):
            if a!=0:
                combo[0]=[combo[0][-1]]+[row for row in combo[0][:n-1]]
            for b in range(n):
                if b!=0:
                    combo[0]=[row[-1]+row[:n-1] for row in combo[0]]
                for c in range(n):
                    if c!=0:
                        combo[1]=[combo[1][-1]]+[row for row in combo[1][:n-1]]
                    for d in range(n):
                        if d!=0:
                            combo[1]=[row[-1]+row[:n-1] for row in combo[1]]
                        #join pieces together
                        joined=[''.join(['#' if combo[0][i][j] is '#' or combo[1][i][j] is '#' else '.' for j in range(n)]) for i in range(n) ]
                        if joined==original:
                            result=str(combo_indexes[0]+1)+' '+str(combo_indexes[1]+1)
                            found=True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        if found:
            break

with open('bcs.out','w') as fout:
    fout.write(result+'\n')
