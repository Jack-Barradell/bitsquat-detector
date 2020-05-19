import re
import sys
import pythonwhois
import time
import getopt

WHOIS_SLEEP = 5
RATE_LIMIT_STRING = ("['clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited', 'clientRenewProhibited https://icann.org/epp#clientRenewProhibited', "
                    + "'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited']")

def usage():
    print("Bitsquat Detector")
    print()
    print("Usage: bitsquat.py -u <url>")
    print("The url prefix is not needed. E.g for www.google.com, only provide \"google.com\"")
    print()
    print("Flags:")
    print("{} - Target url to check".format("\t-u --url".ljust(20, " ")))
    print("{} - Check if domain is registered. NOTE: To prevent rate limiting this slows the program down heavily".format("\t-c --check".ljust(20, " ")))
    print("{} - Show this help message".format("\t-h --help".ljust(20, " ")))
    print()
    print("Examples: bitsquat.py fake-domain.com")
    print()


def main():
    if len(sys.argv) == 1:
        usage()
        sys.exit(1)

    whois_check = False
    whois_rate_limit = False
    target_url = ''
    available_found = 0
    not_available_found = 0

    try:
        opts,args = getopt.getopt(sys.argv[1:],"u:ch",["url","check","help"])
    except getopt.GetoptError as e:
        print(str(e))
        usage()
        sys.exit(1)

    for o,a in opts:
        if o in ("-u", "--url"):
            target_url = a
        elif o in ("-c", "--check"):
            whois_check = target_url
        elif o in ("-h", "--help"):
            usage()
            sys.exit(0)
        else:
            print("[!] Invalid option {} with value {}".format(o,a))
            sys.exit(1)

    # Only want the url name first, so split the tld out
    split_url = target_url.split('.', 1)

    if len(split_url) == 1:
        usage()
        sys.exit(1)

    # Converting the url to a list of binary numbers representing the letters
    binary_list = string_to_binary_list(split_url[0])

    print("[+] Generating bitsquat domains")

    binary_results = []

    # Loop over each letter checking to see if by changing one bit, another valid
    # url character is generated
    for i,byte in enumerate(binary_list):

        # Check if the byte is the first or last in a url
        if i == 0 or i == (len(binary_list) - 1):
            start_end = True
        else:
            start_end = False

        replacements = check_byte(byte, start_end)
        for replacement in replacements:
            test_list = binary_list.copy()
            test_list[i] = replacement
            binary_results.append(test_list)

    print("[+] Finished generating bitsquat domains")

    for binary_result in binary_results:
        binary_result_string = binary_list_to_string(binary_result)

        url = "{}.{}".format(binary_result_string,split_url[1])

        print("[+] Found {}".format(url))

        if whois_check and not whois_rate_limit:
            print("\t[+] Checking if registered")

            whois = pythonwhois.get_whois(url)

            if whois.get('status') and RATE_LIMIT_STRING in whois.get('status'):
                print("[!] Hit whois rate limit, continuing without whois")
                whois_rate_limit = True

            if whois.get('status') and not whois_rate_limit:
                print("\t[-] Not available")
                not_available_found += 1
            else:
                print("\t[+] Available")
                available_found += 1

            print("\t[+] Waiting {} seconds until next check".format(WHOIS_SLEEP))

            # Delay to prevent rate limiting 
            time.sleep(WHOIS_SLEEP)

    print("[+] Completed. Total domains found: {}".format(len(binary_results)))
    if whois_check:
        print("[+] Total available domains: {}".format(available_found))
        print("[+] Total not available domains: {}".format(not_available_found))


# Given a byte of binary data, check to see if by changing any single bit,
# another valid url character is generated
def check_byte(byte, start_end):
    result_letters = []
    bit_list = list(byte)
    for i,bit in enumerate(bit_list):
        test_byte = bit_list.copy()

        if bit =='1':
            test_byte[i] = '0'
        else:
            test_byte[i] = '1'

        char_check = binary_to_string(''.join(test_byte))

        # If the byte is the first or last then exclude characters which
        # can't be in those positions
        if start_end:
            regex = r'[a-zA-Z0-9]'
        else:
            regex = r'[a-zA-Z0-9\-\_]'

        if re.match(regex, char_check):
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
