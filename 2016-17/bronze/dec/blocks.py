import string
import copy

with open('blocks.in','r') as fin:
    lines=fin.readlines()

n=int(lines[0])
boards=[line.split() for line in lines[1:]]

blocks=[0]*26
#iterate through all boards
for board in boards:
    letters=[letter for word in board for letter in word]
    #iterate through all distinct letters and add the side each letter appears more on 
    for letter in set(letters):
        letter_index=string.ascii_lowercase.index(letter)
        blocks[letter_index]+=max(board[0].count(letter),board[1].count(letter))

with open('blocks.out','w') as fout:
    for block in blocks:
        fout.write(str(block)+'\n')
