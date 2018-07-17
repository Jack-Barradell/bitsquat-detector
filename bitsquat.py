import re

def usage():
    print("Bitsquat Detector")
    print()
    print("Usage: bitsquat.py <site name>")
    print("Only the name of the url is needed. E.g for www.google.com, only provide \"google\"")
    print("E.g: bitsquat.py google")
    print()


def main():
    pass


def string_to_binary_list(string):
    return [format(ord(x), 'b') for x in string]


if __name__ == '__main__':
    main()

