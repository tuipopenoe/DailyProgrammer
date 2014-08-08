# Directions

The square-root of 2 is, as Hippasus of Metapontum discovered to his sorrow, 
irrational. Among other things, this means that its decimal expansion goes on 
forever and never repeats.
Here (input.txt) for instance, is the first 100000 digits of the square-root 
of 2.
Except that it's not!
I, evil genius that I am, have changed exactly one of those 100000 digits to 
something else, so that it is slightly wrong. Write a program that finds what 
digit I changed, what I changed it from and what I changed it to.
Now, there are a number of places online where you can get a gigantic decimal 
expansion of sqrt(2), and the easiest way to solve this problem would be to 
simply load one of those files in as a string and compare it to this file, and 
the number would pop right out. But the point of this challenge is to try and 
do it with math, not the internet, so that solution is prohibited!