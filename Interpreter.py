import sys
from PIL import Image

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

# get program data
width, height = program.size
pixels = program.load()

# initialize varlist
varlist = []
for i in range(256):
    var = Var('', False)
    varlist.append(var)

# for each pixel
for y in range(height):
    for x in range(width):

        # get pixel and pixel data
        pixel = pixels[x, y]
        r, g, b, a = pixel

        if a == 0: continue # skip if pixel transparent

        # value character
        if r == 0:

            # for each var in varlist
            building = False
            for i in range(256):

                # if reading var
                if varlist[i].reading:

                    # append value
                    if g == 0: varlist[i].value += chr(b) # ascii
                    elif g == 1: varlist[i].value += str(b) # integer
                    elif g == 2: varlist[i].value += varlist[b].value # variable
                    building = True

            # if not building
            if not building:

                # print character
                if g == 0: print(chr(b), end='') # ascii
                elif g == 1: print(b) # integer
                elif g == 2: print(varlist[b].value) # variable

        # variable definition
        elif r == 1:

            if g == 0: varlist[b] = Var('', True) # start read
            if g == 1: varlist[b].reading = False # end read

