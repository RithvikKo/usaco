with open('censor.in','r') as fin:
    lines=fin.readlines()

s,t=lines[0].strip(),lines[1].strip()

result=s[:len(t)-1]
#iterate through each letter and append letter to result
for letter in s[len(t)-1:len(s)]:
    result+=letter
    #check if the last substring of result is equal to t
    if result[-len(t):]==t:
        #remove last substring
        result=result[:-len(t)]

with open('censor.out','w') as fout:
    fout.write(result+'\n')
