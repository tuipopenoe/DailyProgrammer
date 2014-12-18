## Description

Text formatting is big business. Every day we read information in one of several formats. Scientific publications often have their text split into two columns, like this. Websites are often bearing one major column and a sidebar column, such as Reddit itself. Newspapers very often have three to five columns. You've been commisioned by some bloke you met in Asda to write a program which, given some input text and some numbers, will split the data into the appropriate number of columns.

### Input

To start, you will be given 3 numbers on one line:
<number of columns> <column width> <space width>
number of columns: The number of columns to collect the text into.
column width: The width, in characters, of each column.
space width: The width, in spaces, of the space between each column.
After that first line, the rest of the input will be the text to format.

### Output

You will print the text formatted into the appropriate style.
You do not need to account for words and spaces. If you wish, cut a word into two, so as to keep the column width constant.