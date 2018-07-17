# Bitsquat Detector 

A tool to generate a list of domains which bitsquat a given domain. For further information on bitsquatting I recommend reading http://dinaburg.org/bitsquatting.html

# Installation 

This tool is designed to work on python 3 and has not been tested on python 2.

To install simply clone this repo

    git clone https://github.com/Jack-Barradell/bitsquat-detector

Then setup the primary dependency of pythonwhois

    pip install pythonwhois

Simple, That's it!

# Usage

    Bitsquat Detector
     
    Usage: bitsquat.py -u <url>
    The url prefix is not needed. E.g for www.google.com, only provide "google.com"
     
    Flags:
            -u --url            - Target url to check
            -c --check          - Check if domain is registered. NOTE: To prevent rate limiting this slows the program down heavily
            -h --help           - Show this help message

    Examples: bitsquat.py fake-domain.com

## Examples 

### Just generate domains 

    > python bitsquat.py -u bbc.co.uk 
    [+] Generating bitsquat domains
    [+] Finished generating bitsquat domains
    [+] Found rbc.co.uk
    [+] Found jbc.co.uk
    [+] Found fbc.co.uk
    [+] Found cbc.co.uk
    [+] Found brc.co.uk
    [+] Found bjc.co.uk
    [+] Found bfc.co.uk
    [+] Found bcc.co.uk
    [+] Found bbs.co.uk
    [+] Found bbk.co.uk
    [+] Found bbg.co.uk
    [+] Found bba.co.uk
    [+] Found bbb.co.uk
    [+] Completed. Total domains found: 13

### Generate domains and check them

    > python .\bitsquat.py -u microsoft.com -c
    [+] Generating bitsquat domains
    [+] Finished generating bitsquat domains
    [+] Found eicrosoft.com
            [+] Checking if registered
            [-] Not available
            [+] Waiting 5 seconds until next check
    [+] Found iicrosoft.com
            [+] Checking if registered
            [+] Available
            [+] Waiting 5 seconds until next check
    [+] Found oicrosoft.com
            [+] Checking if registered
            [-] Not available
            [+] Waiting 5 seconds until next check
    [+] Found licrosoft.com
           [+] Checking if registered
            [-] Not available
            [+] Waiting 5 seconds until next check
    [+] Found mycrosoft.com
            [+] Checking if registered
            [-] Not available
            [+] Waiting 5 seconds until next check
    [+] Found macrosoft.com
            [+] Checking if registered
            [-] Not available
            [+] Waiting 5 seconds until next check
    [+] Found mmcrosoft.com
            [+] Checking if registered
            [-] Not available
            [+] Waiting 5 seconds until next check
    <OUTPUT SNIPPED>
    [+] Completed. Total domains found: 43

## Errors 

When using the -c option, you may encounter the following error 

    [!] Hit whois rate limit, continuing without whois

This occurs when too many requests have been made to check domain availability and will disable domain availability checking for the remainder of the session.

# Disclaimer 

All code and tools are provided for educational purposes and I can accept no responsibilty for misuse. 