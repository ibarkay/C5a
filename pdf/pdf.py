
import re

fily = open('ob69allv.txt', 'r') # in this file all the changes in object 69 in pdf (object 69 is the only change)
fily = fily.read()



regex = re.findall('Contents \d{1,2}',fily) # finde all contens

jumps = re.findall('\d{1,2}',str(regex)) #finde all numbers
print jumps

hash = 'I1OmhQsgalpD}v8W3GNC7ZHbTUYKt5n90y_dEzFk4eiPL{oAJu6fMjrc2wxSRqBXV' # i "read between the lines" of all objects stream got the one char


cracked = ''

for i in jumps:
    cracked += hash[int(i)-1] # lets get this MF flag !

print cracked

