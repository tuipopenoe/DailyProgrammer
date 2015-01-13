## Description
You and a few co-workers are implementing a cool new technology called "blue-steel" (not to be confused with this awesome feat of technology). Part of this technology, specifically the part assigned to you, is to check what "type" a given string of information is. Blue-steel currently must distinguish between a signed integer, signed float, a date, and a text-string.
Your goal is to write a function which, given a string of text, will echo out what "type" the string is. The string could be a signed integer (a series of digits with either a + or - at the front, though the + is optional), a signed float (a series of digits with either a + or - at the front, though the + is optional, and a . to distinguish the left and right hand digits), a date (which will be in the format of "day-month-year"), and finally a string of text (any other data). The given string will always be just one type at a time.

### Input
String TypeString - A string to test what type it is.

#### Sample Input
"123"

### Output
You must print either "int", "float", "date", or "text" after identifying what string type this is.

#### Sample Output
"int"