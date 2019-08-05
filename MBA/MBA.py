import glob
import base64

#print(glob.glob("fs/mes*"))


fname = ''

def read_msgB64():
    listy = []
    for i in glob.glob('fs/mes*'):
        fname = str(i)
        fily = open(fname, 'r')
        fily = fily.read()
        listy.append([fily.decode('base64'),fname])
    return listy

filysh = open('bin_try','wb')


def reaf_binar():
    for i in SderofBins:
        fname = i

        with open(fname, "rb") as f:
            byte = f.read(1)
            while byte != "":
                # Do stuff with byte.
                byte = f.read(1)
                filysh.write(byte)
#print read_msgB64()

sentense = "One must divide one's time between politics and equations. But our equations are much more important to me, because politics is for the present, while our equations are for eternity."

sentense = sentense.split(' ')
#print sentense


Seder = []
for i in sentense:
    for j in read_msgB64():
        if j[0] == i :
            Seder.append([j,int(sentense.index(i))])

SderofBins = []
for i in Seder:
    SderofBins.append(i[0][1].replace('message','bin'))
print SderofBins


def Sort(sub_li):

    sub_li.sort(key=lambda x: x[1])
    return sub_li

reaf_binar()


