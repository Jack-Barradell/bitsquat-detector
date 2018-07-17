import re
import sys

def usage():
    print("Bitsquat Detector")
    print()
    print("Usage: bitsquat.py <site name>")
    print("Only the name of the url is needed. E.g for www.google.com, only provide \"google\"")
    print("E.g: bitsquat.py google")
    print()


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    binary_list = string_to_binary_list(sys.argv[1])


def string_to_binary_list(string):
    return [format(ord(x), 'b') for x in string]


def binary_list_to_string(binary_list):
    return ''.join(chr(int(char, 2)) for char in binary_list)


if __name__ == '__main__':
    main()