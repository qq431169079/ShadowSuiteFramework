#!/usr/bin/env python

import os
import sys

def main():
    try:
        print('Importing time module...')
        import time
        time.sleep(1)
    
    except ImportError:
        print('Error importing module!')
        sys.exit(1)

    try:
        print('Importing API module...')
        import API
        time.sleep(1)

    except ImportError:
        print('Error importing module!')
        sys.exit(1)

    print('Preparing to test API...')
    time.sleep(3)

    try:
        print('Testing error module...')
        print()
        print(API.error.error0001)
        print()
        print(API.error.error0002)
        print()
        print(API.error.error0003)
        print()
        print(API.error.error0004)
        print()
        print(API.error.error0005)
        print()
        print(API.error.error0006)
        print()
        print(API.error.error0007)
        print()
        print(API.error.error0008)
        print()
        print(API.error.warning0001)
        print()
        print(API.error.warning0002)
        print()
        time.sleep(1)

    except:
        print('Error while testing error module...')
        sys.exit(1)

    try:
        print('Testing misc module...')
        print()
        print(API.misc.logo)
        print()
        print(API.misc.module_mode_info)
        print()
        print('Skipping program_restart()')
        print()
        time.sleep(1)

    except:
        print('Error while testing misc module...')
        sys.exit(1)

if __name__ == '__main__':
    main()
