## Description
Today we will be making some simple 8x8 bitmap pictures. You will be given 8 hex values that can be 0-255 in decimal value (so 1 byte). Each value represents a row. So 8 rows of 8 bits so a 8x8 bitmap picture.

### Input
8 Hex values.
example:
18 3C 7E 7E 18 18 18 18

### Output
A 8x8 picture that represents the values you read in.
For example say you got the hex value FF. This is 1111 1111 . "1" means the bitmap at that location is on and print something. "0" means nothing is printed so put a space. 1111 1111 would output this row:
xxxxxxxx
if the next hex value is 81 it would be 1000 0001 in binary and so the 2nd row would output (with the first row)
xxxxxxxx
x      x