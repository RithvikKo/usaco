alphabet=input()
bessie=input()

letter=result=0
done=False
#iterate through all letters
while not done:
	#iterate through alphabet
    for i in alphabet:
        if i==bessie[letter]:
            letter+=1
            if letter==len(bessie):
                done=True
                break
    result+=1

print(result)
