import glob
import base64

#print(glob.glob("fs/mes*"))


fname = ''

def read_msgB64():
    for i in glob.glob('fs/mes*'):
        fname = str(i)
        fily = open(fname, 'r')
        fily = fily.read()
        print fily.decode('base64'),

def reaf_binar():
    for i in glob.glob('fs/bin_se*'):
        fname = str(i)

        with open(fname, "rb") as f:
            byte = f.read(1)
            while byte != "":
                # Do stuff with byte.
                byte = f.read(1)
                #if byte.isalpha():
                print byte,
read_msgB64()
reaf_binar()








