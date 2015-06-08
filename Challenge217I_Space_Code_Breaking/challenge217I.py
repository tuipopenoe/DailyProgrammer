#/usr/bin/env python
# Tui Popenoe
# Challenge217I.py Space Code Breaking

from sys import argv

def omicron_v(code):
    """Return the decoded omicron_v string."""
    output = []
    for i in code:
        bin_rep = bin8(int(i))
        swap = list(bin_rep)
        swap[2] = '0' if swap[2] == '1' else  '1'
        output.append(int(''.join(swap), 2))
    return ''.join(output)

def hoth(code):
    """Return the decoded hoth string."""
    output = []
    for j in code:
        output.append(chr(int(j) + 10))
    return ''.join(output)

def ryza_iv(code):
    """Return the decoded ryaz_iv string."""
    output = []
    for k in code:
        output.append(chr(int(k) - 1))
    return ''.join(output)

def htrae(code):
    """Return the decoded htrae string."""
    output = []
    for l in code:
        output.append(chr(int(l)))
    return ''.join(output)[::-1]

def is_english(string, dct):
    """Check if the word exists in the given English dictionary."""
    for word in string:
        if word not in dct:
            return False
    return True

def load_dictionary(filename):
    with open(filename) as f:
        return {word.strip().lower(): index for (index, word) in f.read().split()} 
    return {}

def bin8(integer):
    """Return the 8 digit binary format of the given integer."""
    return format(integer, '08b')

def decrypt_code(input_string):
    """Decrypt the input code."""
    code = input_string.split()
    dct = load_dictionary('dictionary.txt')
    omicron_v_str = omicron_v(code)
    hoth_str = hoth(code)
    ryza_iv_str = ryza_iv(code)
    htrae_str = htrae(code)
    if is_english(omicron_v_str, dct):
        return "Omicron V: %s" % (omicron_v_str)
    if is_english(hoth_str, dct):
        return "Hoth: %s" % (hoth_str)
    if is_english(ryza_iv_str, dct):
        return "Ryza IV: %s" % (ryza_iv_str)
    if is_english(htrae_str, dct):
        return "Htrae: %s" % (htrae_str)

    return "Untranslatable code: %s\n%s\n%s\n%s" % (omicron_v_str, hoth_str, ryza_iv_str, htrae_str)

def main():
    if len(argv) > 1:
        print(decrypt_code(argv[1]))
    else:
        print(decrypt_code(raw_input("Enter the code to decrypt: ")))

if __name__ == '__main__':
    main()

