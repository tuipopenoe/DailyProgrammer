## Description
Write a program that takes two integers, N and M, and find the largest integer composed of N-digits that is evenly divisible by M. N will always be 1 or greater, with M being 2 or greater. Note that some combinations of N and M will not have a solution.
Example: if you are given an N of 3 and M of 2, the largest integer with 3-digits is 999, but the largest 3-digit number that is evenly divisible by 2 is 998, since 998 Modulo 2 is 0. Another example is where N is 2 and M is 101. Since the largest 2-digit integer is 99, and no integers between 1 and 99 are divisible by 101, there is no solution.

### Input
You will be given two integers, N and M, on standard console input. They will be space delimited values where N will range from 1 to 9, and M will range from 2 to 999,999,999.


### Output
Print the largest integer within the range of 1 to the largest integer formed by N-digits, that is evenly-divisible by the integer M. You only need to print the largest integer, not the set of evenly-divisible integers. If there is no solution, print "No solution found".