from PIL import Image

# open program and get data
program = Image.open('./program.png')
width, height = program.size
pixels = program.load()

# initialize varlist
varlist = []
for i in range(256): varlist.append(0)

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

        # variable definition
        elif r == 1: varlist[b] = g

        # print variable
        elif r == 2:

            if g == 0: print(chr(varlist[b]), end='') # ascii
            elif g == 1: print(varlist[b]) # integer
