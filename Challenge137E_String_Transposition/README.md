## Description
It can be helpful sometimes to rotate a string 90-degrees, like a big vertical "SALES" poster or your business name on vertical neon lights, like this image from Las Vegas. Your goal is to write a program that does this, but for multiples lines of text. This is very similar to a Matrix Transposition, since the order we want returned is not a true 90-degree rotation of text.


### Input
You will first be given an integer N which is the number of strings that follows. N will range inclusively from 1 to 16. Each line of text will have at most 256 characters, including the new-line (so at most 255 printable-characters, with the last being the new-line or carriage-return).

### Output
Simply print the given lines top-to-bottom. The first given line should be the left-most vertical line.