from PIL import Image

# open program and get data
program = Image.open('./program.png')
width, height = program.size
pixels = program.load()

# variable class
class Var:

    def __init__(self, value, building):
        self.value = value
        self.building = building
        
    value = ''
    building = False

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

        # skip if alpha 0
        if a == 0: continue

        # print character
        if r == 0:

            if g == 0: print(chr(b), end='') # ascii
            elif g == 1: print(b) # integer

        # toggle variable definition
        elif r == 2:

            if g == 0: varlist[b] = Var('', True) # start read
            if g == 1: varlist[b] = Var('', False) # end read

        # print variable
        elif r == 3: print(varlist[b].value)
