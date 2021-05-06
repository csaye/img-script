# ImgScript
An image-based programming language.

## Interpreter

The interpreter takes an image as input and processes the pixels from top left to bottom right.

A pixel with an alpha of zero will be skipped.

The r value determines the function, the g value determines the function type, and the b value determines the function value.

r0 : value
- g0: ascii
- g1: integer
- g2: variable
  - b: value

r1 : variable
- g0 : start read
- g1: end read
  - b: variable index
