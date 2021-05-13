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
        
    value = ''
    reading = False

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
    if a == 0 or r != 0: return ''

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
        val = str(value(pixel))

        # for each var in varlist
        building = False
        for i in range(256):

            # if reading var
            if varlist[i].reading:

                # append value
                varlist[i].value += val
                building = True

        # if not building
        if not building:

            # print character
            if g == 0: print(val, end='') # ascii
            else: print(val) # all other values

    # variable definition
    elif r == 1:

        if g == 0: varlist[b] = Var('', True) # start read
        if g == 1: varlist[b].reading = False # end read

    # if statement
    elif r == 2:

        term1 = value(pixels[index + 1]) # term 1
        operation = value(pixels[index + 2]) # operation
        term2 = value(pixels[index + 3]) # term 2
        result = value(pixels[index + 4]) # result

    # goto statement
    elif r == 3:

        if g == 0: index = b - 1 # go to pixel count
        elif g == 1: index += b # skip forward pixels
        elif g == 2: index -= b # skip backward pixels
        elif g == 3: index = len(pixels) # go to end

# loop through pixels
index = 0
while index < len(pixels):

    # process index and increment
    process(index)
    index += 1
