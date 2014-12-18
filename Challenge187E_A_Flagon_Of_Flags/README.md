## Description

In the command-line world, programs are operated not with graphical user interfaces but with command line flags. These flags are what the operator uses to pass parameters to the program. The standard form of flag starts with a double hyphen -- and consists of a word in lower-case-separated-by-hyphens. For example, to forcefully remove a directory recursively on Unix based systems, the command used may be:
rm --recursive --force dir/
Here, the recursive and force flags have been enabled, which the program detects and changes its behaviour accordingly. Alternatively, many programs allow a short-form of command-line flag. These flags are one letter long andn start with a single hyphen -. For example, the above command can be reduced to:
rm -r -f dir/
This is much shorter, so commonly used flags are often abbreviated as such. An even shorter form merges several of these flags into one flag. This is still separated by a hyphen but consists of multiple letters. For example, in the tar command on Unix based systems, the -x -z -v flags can be merged into -xzv with the exact same meaning. The above rm command looks like this:
rm -rf dir/
This is even more convenient for a terminal operator to enter. Today, you will write a program which will accept a string of flags in the above formats and output which flags were activated.

### Input

You will first input a number N. You will then accept N lines of input in the format:
f:force
This is a short-form definition; this particular example denotes that the flag -f is equivalent to the flag --force. Lastly you are to accept one further line of input containing the flags and other parameters passed to the program. Remember that programs can accept parameters that are not flags. These don't start with a hyphen and there may be several of them. For example,
-Q -rf --no-preserve-root directory1/ directory2/
In which the flags given are -Q -rf (same as -r -f) and --no-preserve-root, and the parameters are directory1/ and directory2/. Remember the Q, r and f flags are defined in the short-form definition format above.

### Output

You are to output a list of the full names of all of the flags entered (eg. force rather than f), as well as all of the parameters entered. Alternatively, if a short-form flag is entered that doesn't have a difinition, print an error.