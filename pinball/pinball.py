import re
table = open('t.txt', 'r')

table = table.readlines()


list_of_keys = []

for i in table:
    list_of_keys.append(str(i).replace('\n','').split(' '))

new_list = []

for i in list_of_keys:
    for j in i:
        new_list.append(j)

newnew_list = []

for i in new_list:
    newnew_list.append(int(str(i).strip('\'')))



print newnew_list

stringy = []

for i in newnew_list:

    a = hex(i)
    hex_int = int(a, 16)
    b = 0x7f
    new_int = hex_int ^ b
    try:
        stringy.append(str(hex(new_int)[2:]).decode('hex') + ' the Key was : ' + str(i))
    except:
        pass

for i in stringy:
    if i[0].isupper():
        print i






'''F'''






'''k = []
for i in newnew_list:
    k.append('0x'+hex(int(i)).split('x')[-1])

print k'''

