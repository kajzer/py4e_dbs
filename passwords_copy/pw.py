#!/usr/bin/env python3
# pw.py - An insecure password locker program.
import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
             

def main():
    if len(sys.argv) < 2:
        print('Usage: ./pw.py [account] - copy account password')
        print('Needs file permissions with: sudo chmod +x pw.py')
        print('Alternative usage: python3 pw.py [account] - copy account password')
        sys.exit()
    account = sys.argv[1]
    
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)

if __name__ == "__main__":
    main()