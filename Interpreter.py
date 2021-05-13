import sys, operator
from PIL import Image

# operators
operators = [
    operator.add,
    operator.sub,
    operator.mul,
    operator.truediv,
    operator.pow,
    operator.mod,
    operator.floordiv
]

# variable class
class Var:

    def __init__(self, value, reading):
        self.value = value
        self.reading = reading

# open program
try:
    program = Image.open('./program.png')
# fail open
except:
    print('No program.png file found.')
    sys.exit()

# initialize varlist
varlist = []
for i in range(256):
    var = Var('', False)
    varlist.append(var)

# get program data
width, height = program.size
pix = program.load()

# create pixels array
pixels = []
for y in range(height):
    for x in range(width):
        pixel = pix[x, y]
        pixels.append(pixel)

# returns value of given value pixel
def value(pixel):

    # get pixel data
    r, g, b, a = pixel

    # return if empty or not value pixel
    if a == 0 or r != 0: return None

    # return value
    if g == 0: return chr(b) # ascii
    elif g == 1: return b # integer
    elif g == 2: return varlist[b].value # variable
    elif g == 3: return operators[b] # operator

# processes pixel of given index
def process(i):
    global index

    # get pixel and pixel data
    pixel = pixels[i]
    r, g, b, a = pixel

    if a == 0: return # skip if pixel transparent

    # value character
    if r == 0:

        # get value as string
        val = value(pixel)

        # for each var in varlist
        building = False
        for i in range(256):

            # if reading var
            if varlist[i].reading:

                # append value
                if varlist[i].value == None: varlist[i].value = val
                else: varlist[i].value += val
                building = True

        # if not building
        if not building:

            # print character
            if g == 0: print(val, end='') # ascii
            else: print(val) # all other values

    # variable definition
    elif r == 1:

        # read
        if g == 0: varlist[b] = Var(None, True) # start read
        elif g == 1: varlist[b].reading = False # end read

        # modify
        elif g == 2: varlist[b].value += 1 # add 1
        elif g == 3: varlist[b].value -= 1 # sub 1

    # if statement
    elif r == 2:

        # two term statement
        if g >= 0 and g < 4:

            # get statement values
            term1 = value(pixels[index + 1]) # term 1
            term2 = value(pixels[index + 2]) # term 2

            index += 2 # skip if statement pixels

            if g == 0 and term1 != term2: index += b # equals
            elif g == 1 and term1 == term2: index += b # not equals
            elif g == 2 and term1 <= term2: index += b # greater than
            elif g == 3 and term1 >= term3: index += b # less than

        # three term statement
        if g >= 4 and g < 8:

            # get statement values
            term1 = value(pixels[index + 1]) # term 1
            operation = value(pixels[index + 2]) # operation
            term2 = value(pixels[index + 3]) # term 2
            term3 = value(pixels[index + 4]) # term 3

            index += 4 # skip if statement pixels

            # if statement does not pass, skip pixels
            if g == 4 and operation(term1, term2) != term3: index += b # equals
            elif g == 5 and operation(term1, term2) == term3: index += b # not equals
            elif g == 6 and operation(term1, term2) <= term3: index += b # greater than
            elif g == 7 and operation(term1, term2) >= term3: index += b # less than

    # goto statement
    elif r == 3:

        if g == 0: index = b - 1 # go to pixel count
        elif g == 1: index += b # skip forward pixels
        elif g == 2: index -= b # skip backward pixels
        elif g == 3: index = len(pixels) # go to end

# print pixel data
rgbs = []
for pixel in pixels:
        r, g, b, a = pixel # get pixel data
        if a == 0: continue # skip pixel if empty
        rgbs.append(f'({r}, {g}, {b})') # append pixel to rgbs list

# print pixel list
print('Processing program.png:')
print(', '.join(rgbs))
print('----------------')

# loop through pixels
index = 0
while index < len(pixels):

    # process index and increment
    process(index)
    index += 1
