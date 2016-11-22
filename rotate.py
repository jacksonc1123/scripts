#!/usr/bin/python2

def rotate(rot):
    """ Perform a rot17 operation """
    chars = []
    for s in rot:
        i = ord(s)+17
        if i > 126:
            temp = i - 126
            chars.append(chr(33+temp))
        else:
            chars.append(chr(i))
    return ''.join(chars)

def main():
    rot = raw_input("Rotate: ")
    print rotate(rot)

if __name__ == "__main__":
    main()
