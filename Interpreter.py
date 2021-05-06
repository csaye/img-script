from PIL import Image

# open program and get data
program = Image.open('./program.png')
width, height = program.size
pixels = program.load()

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
            print(chr(g + b), end='')
