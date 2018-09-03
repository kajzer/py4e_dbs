#!/usr/bin/env python3
# mapit.py - get google maps with command line arguments

import webbrowser, sys, pyperclip

def main():
    if len(sys.argv) > 1:
        # Get addres from command line
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard
        address = pyperclip.paste()
    
    webbrowser.open('https://www.google.com/maps/place/' + address)
    
if __name__ == "__main__":
    main()