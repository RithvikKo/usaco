import itertools

with open('tttt.in','r') as fin:
    lines=fin.readlines()

board=[line for line in lines]
unique=list(set(i for line in lines for i in line))

one=0
#find all individual cows that can claim victory
for cow in unique:
    if {board[0][0],board[1][1],board[2][2]}=={cow}:
        one+=1
    elif {board[0][2],board[1][1],board[2][0]}=={cow}:
        one+=1
    else:
        for i in range(3):
            if {board[i][0],board[i][1],board[i][2]}=={cow}:
                one+=1
                break
            elif {board[0][i],board[1][i],board[2][i]}=={cow}:
                one+=1
                break

two=0
teams=itertools.combinations(unique,2)
#find all teams of two cows that can claim victory
for team in teams:
    if {board[0][0],board[1][1],board[2][2]}==set(team):
        two+=1
    elif {board[0][2],board[1][1],board[2][0]}==set(team):
        two+=1
    else:
        for i in range(3):
            if {board[i][0],board[i][1],board[i][2]}==set(team):
                two+=1
                break
            elif {board[0][i],board[1][i],board[2][i]}==set(team):
                two+=1
                break

with open('tttt.out','w') as fout:
    fout.write(str(one)+'\n')
    fout.write(str(two)+'\n')
