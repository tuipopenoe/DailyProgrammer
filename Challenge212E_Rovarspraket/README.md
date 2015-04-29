## Description
Your task today is to write a program that can encode a string of text into Rövarspråket.

### Input
You will recieve one line of input, which is a text string that should be encoded into Rövarspråket.

### Output
The output will be the encoded string.
A few notes: your program should be able to handle case properly, which means that "Hello" should be encoded to "Hohelollolo", and not as "HoHelollolo" (note the second capital "H").
Also, since Rövarspråket is a Swedish invention, your program should follow Swedish rules regarding what is a vowel and what is a consonant. The Swedish alphabet is the same as the English alphabet except that there are three extra characters at the end (Å, Ä and Ö) which are all vowels. In addition, Y is always a vowel in Swedish, so the full list of vowels in Swedish is A, E, I, O, U, Y, Å, Ä and Ö. The rest are consonants.
Lastly, any character that is not a vowel or a consonant (i.e. things like punctuation) should be left intact in the output.


#### Sample Input
Jag talar Rövarspråket!


#### Sample Output
Jojagog totalolaror Rorövovarorsospoproråkoketot!