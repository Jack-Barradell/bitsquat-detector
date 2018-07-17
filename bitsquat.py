import re
import sys

def usage():
    print("Bitsquat Detector")
    print()
    print("Usage: bitsquat.py <url>")
    print("The url prefix is not needed. E.g for www.google.com, only provide \"google.com\"")
    print("E.g: bitsquat.py fake-domain.com")
    print()


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    split_url = sys.argv[1].split('.', 1)

    if len(split_url) == 1:
        usage()
        sys.exit(1)

    binary_list = string_to_binary_list(split_url[0])


    binary_results = []
    for i,byte in enumerate(binary_list):
        replacements = check_byte(byte)
        for replacement in replacements:
            test_list = binary_list.copy()
            test_list[i] = replacement
            binary_results.append(test_list)

    for binary_result in binary_results:
        binary_result_string = binary_list_to_string(binary_result)
        print("{}.{}".format(binary_result_string,split_url[1]))


def check_byte(byte):
    result_letters = []
    bit_list = list(byte)
    for i,bit in enumerate(bit_list):
        test_byte = bit_list.copy()
        if bit =='1':
            test_byte[i] = '0'
        else:
            test_byte[i] = '1'
        char_check = binary_to_string(''.join(test_byte))
        if re.match(r'[a-zA-Z0-9]', char_check):
            original_char = binary_to_string(str(byte))
            if not original_char.lower() == char_check.lower():
                result_letters.append(''.join(test_byte))
    return result_letters


def string_to_binary_list(string):
    return [format(ord(x), 'b') for x in string]


def binary_list_to_string(binary_list):
    return ''.join(binary_to_string(char) for char in binary_list)


def binary_to_string(binary):
    return str(chr(int(binary, 2)))

if __name__ == '__main__':
    main()