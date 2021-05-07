# ImgScript
An image-based programming language.

## Interpreter

The interpreter takes an image as input and processes the pixels from top left to bottom right.

A pixel with an alpha of zero will be skipped.

The r value determines the function, the g value determines the function type, and the b value determines the function value.

## Functions

- r0 (value)
  - g0 (ascii)
  - g1 (integer)
  - g2 (variable)
  - g3 (operator)
    - b (value)
- r1 (variable)
  - g0 (start read)
  - g1 (end read)
    - b (variable index)
- r2 (if statement)
  - g0 (equals)
  - g1 (not equals)
  - g2 (greater than)
  - g3 (less than)
    - b (pixels to skip if false)
  - pixel + 1 - term 1
  - pixel + 2 - operation
  - pixel + 3 - term 2
  - pixel + 4 - result

## Examples

Hello World

![](https://user-images.githubusercontent.com/27871609/117510020-87748a80-af48-11eb-9c59-73dff99db74b.png)

(0, 0, 72), (0, 0, 101), (0, 0, 108), (0, 0, 108), (0, 0, 111), (0, 0, 32), (0, 0, 87), (0, 0, 111), (0, 0, 114), (0, 0, 108), (0, 0, 100), (0, 0, 10)

More examples in [examples folder](examples).
