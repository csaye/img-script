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

        if a == 0: continue # skip if pixel transparent

        # value character
        if r == 0:

            # for each var in varlist
            for i in range(256):

                # if building var
                if varlist[i].building:

                    # append value
                    if g == 0: varlist[i].value += chr(b) # ascii
                    elif g == 1: varlist[i].value += str(b) # integer

        # print character
        elif r == 1:
            
            if g == 0: print(chr(b), end='') # ascii
            elif g == 1: print(b) # integer

        # toggle variable definition
        elif r == 2:

            if g == 0: varlist[b] = Var('', True) # start read
            if g == 1: varlist[b] = Var('', False) # end read

        # print variable
        elif r == 3: print(varlist[b].value)
