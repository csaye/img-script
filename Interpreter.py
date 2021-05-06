from PIL import Image

# open program and get data
program = Image.open('./program.png')
width, height = program.size
pixels = program.load()

# for each pixel
for y in range(height):
    for x in range(width):

        # process pixel
