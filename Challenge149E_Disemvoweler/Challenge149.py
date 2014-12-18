# Tui Popenoe
# Challenge 149 Disemvoweler

def disemvowel(string):
    output = list()
    removed = list()
    vowels = ['a', 'e', 'i', 'o', 'u', ' ']
    for i in string:
        if i not in vowels:
            output.append(i)
        elif i in vowels[:-1]:
            removed.append(i)

    return [''.join(output), ''.join(removed)]