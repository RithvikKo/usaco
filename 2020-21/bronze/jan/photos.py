n=int(input())
ids=list(map(int,input().split()))

evens=0
odds=0
#count number of evens and odds
for id in ids:
    if id%2:
        odds+=1
    else:
        evens+=1

#if there are no odds, we can only have one group
if odds==0:
    result=1
else:
    result=0
    even=True
    #iterate until we run out of cows
    while evens>0 or odds>0:
        if even:
            if evens>0:
                evens-=1
            elif odds>1:
                odds-=2
            #break if there are no more evens and not enough odds to make an even
            else:
                result-=1
                break
        else:
            if odds>0:
                odds-=1
            #break if there are no more odds
            else:
                break
        result+=1
        even=not even

print(result)
