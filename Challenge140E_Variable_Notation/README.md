## Description
When writing code, it can be helpful to have a standard (Identifier naming convention) that describes how to define all your variables and object names. This is to keep code easy to read and maintain. Sometimes the standard can help describe the type (such as in Hungarian notation) or make the variables visually easy to read (CamcelCase notation or snake_case).
Your goal is to implement a program that takes an english-language series of words and converts them to a specific variable notation format. Your code must support CamcelCase, snake_case, and capitalized snake_case.

### Input
On standard console input, you will be given an integer one the first line of input, which describes the notation you want to convert to. If this integer is zero ('0'), then use CamcelCase. If it is one ('1'), use snake_case. If it is two ('2'), use capitalized snake_case. The line after this will be a space-delimited series of words, which will only be lower-case alpha-numeric characters (letters and digits).


### Output
Simply print the given string in the appropriate notation.