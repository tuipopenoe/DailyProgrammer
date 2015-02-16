## Description
You are going to write a home-work helper tool for high-school students who are learning C for the first time. These students are in the advanced placement math course, but do not know anything about programming or formal languages of any kind. However, they do know about functions and variables!
They have been given an 'input guide' that tells them to write simple pure mathematical functions like they are used to from their homework with a simple subset grammar.They are allowed to use sqrt,abs,sin,cos,tan,exp,log, and the mathematical arithmetic operators +*/-, they can name their functions and variables any lower-case alphanumeric name and functions can have between 0 and 15 arguments.
In the this challenge, your job is to write a program that can take in their "simple format" mathematical function and output the correct C syntax for that function. All arguments should be single precision, and all functions will only return one float.

### Input
f(x)=x*x
big(x,y)=sqrt(x+y)*10

### Output
As an example, the input
L0(x,y)=abs(x)+abs(y) 
should output
float L0(float x,float y)
{
    return fabsf(x)+fabsf(y);
}

Bonus points if you support exponentiation with "^", as in "f(x)=x^2"