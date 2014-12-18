## Description
Disemvoweling means removing the vowels from text. (For this challenge, the letters a, e, i, o, and u are considered vowels, and the letter y is not.) The idea is to make text difficult but not impossible to read, for when somebody posts something so idiotic you want people who are reading it to get extra frustrated.
To make things even harder to read, we'll remove spaces too. For example, this string:
two drums and a cymbal fall off a cliff
can be disemvoweled to get:
twdrmsndcymblfllffclff
We also want to keep the vowels we removed around (in their original order), which in this case is:
ouaaaaoai

### Input
A string consisting of a series of words to disemvowel. It will be all lowercase (letters a-z) and without punctuation. The only special character you need to handle is spaces.


### Output
Two strings, one of the disemvoweled text (spaces removed), and one of all the removed vowels.