from tika import parser
import re

from tika import parser


#### global values ###

fileo = 'START.pptx'
slideNumber = 0
key = ''



def get_slides(filey):
    pptx = parser.from_file(filey)
    result = pptx["content"]
    result = result.strip()

    # list of slides
    slides = re.findall('.,\s\w{10}.pptx,\s\d{1,3}',result)  # regulr exprtion of data
    return slides


def get_values_from_slides(file,number):
    # get values - char , next file , slide numbers in that file
    #set global vars
    global fileo
    global key
    global slideNumber

    values = str(file[number]).split(',')
    chary = values[0]
    next_file = values[1][1:]
    slide_number_next_file = values[2][1:]

    print 'the values of slide :char - {}, net file - {} , slide # is {}'.format(chary,next_file,slide_number_next_file)

    key += chary
    fileo = next_file
    slideNumber = int(slide_number_next_file)-1





###########  excute ##########

for x in range(300):
    get_values_from_slides(get_slides(fileo),slideNumber)
    print key


