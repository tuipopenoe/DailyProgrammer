## Description

For those that don't tweet or know the workings of Twitter, you can reply to 'tweets' by replying to that user with an @ symbol and their username.
Here's an example from John Carmack's twitter.
His initial tweet
@ID_AA_Carmack : "Even more than most things, the challenges in computer vision seem to be the gulf between theory and practice."
And a reply
@professorlamp : @ID_AA_Carmack Couldn't say I have too much experience with that
You can see, the '@' symbol is more or less an integral part of the tweet and the reply. Wouldn't it be neat if we could think of names that incorporate the @ symbol and also form a word?
e.g.
@tack -> (attack)
@trocious ->(atrocious)

### Input

As input, you should give a word list for your program to scout through to find viable matches. The most popular word list is good ol' enable1.txt
/u/G33kDude has supplied an even bigger text file. I've hosted it on my site over here , I recommend 'saving as' to download the file.

### Output

Both outputs should contain the 'truncated' version of the word and the original word. For example.
@tack : attack
There are two outputs that we are interested in:
The 10 longest twitter handles sorted by length in descending order.
The 10 shortest twitter handles sorted by length in ascending order.