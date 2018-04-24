#!/usr/bin/env python3

import os
import sys

def main():
    try:
        print('Importing time module...')
        import time
        time.sleep(1)
    
    except ImportError:
        print('Error importing time module!')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Importing traceback module...')
        import traceback
        time.sleep(1)

    except ImportError:
        print('Error importing traceback module...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Importing API module...')
        import API
        time.sleep(1)

    except ImportError:
        print('Error importing API module!')
        traceback.print_exc()
        sys.exit(1)

    print('Preparing to test API...')
    time.sleep(3)

    try:
        print('Testing error module...')
        print()
        print(API.error.ERROR0001)
        print()
        print(API.error.ERROR0002)
        print()
        print(API.error.ERROR0003)
        print()
        print(API.error.ERROR0004)
        print()
        print(API.error.ERROR0005)
        print()
        print(API.error.ERROR0006)
        print()
        print(API.error.ERROR0007)
        print()
        print(API.error.ERROR0008)
        print()
        print(API.error.ERROR0009)
        print()
        print(API.error.ERROR0010)
        print()
        print(API.error.ERROR0011)
        print()
        print(API.error.WARNING0001)
        print()
        print(API.error.WARNING0002)
        print()
        time.sleep(1)

    except:
        print('Error while testing error module...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Testing misc module...')
        print()
        print(API.misc.LOGO)
        print()
        print(API.misc.MODULE_MODE_INFO)
        print()
        print('Skipping program_restart()')
        print()
        time.sleep(1)

    except:
        print('Error while testing misc module...')
        traceback.print_exc()
        sys.exit(1)

    print('Skipping update module...')

    try:
        print('Testing version module...')
        print()
        print(API.version.VNUMBER)
        print()
        print(API.version.VTYPE)
        print()
        print(API.version.VCODENAME)
        print()
        print(API.version.BOTH)
        print()
        time.sleep(1)

    except:
        print('Error while testing version module...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Testing quote module...')
        quotes = 9
        counter = 0
        while counter != quotes:
            quote = API.quote.quote()
            print(quote)
            counter += 1

    except:
        print('Error while testing quote module...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Testing joke module...')
        jokes = 9
        count = 0
        while count != jokes:
            joke = API.joke.joke()
            print(joke)
            count += 1

    except:
        print('Error while testing joke module...')
        traceback.print_exc()
        sys.exit(1)

    print('Skipping logger module...')

    try:
        print('Testing ShadowSuiteLE class variables...')
        print()
        print(API.ShadowSuiteLE().API_VERSION)
        print()
        print(API.ShadowSuiteLE().SHADOWSUITE_VER_NUM)
        print()
        print(API.ShadowSuiteLE().SHADOWSUITE_VER_TYPE)
        print()
        print(API.ShadowSuiteLE().SHADOWSUITE_VER_CODENAME)
        print()
        print(API.ShadowSuiteLE().FINISH)

    except:
        print('Error while testing ShadowSuiteLE class variables...')
        traceback.print_exc()
        sys.exit(1)

    print('Skipping ShadowSuiteLE class generate_new_module method...')

    try:
        print('Testing ShadowSuiteLE class list_module method...')
        print()
        API.ShadowSuiteLE().list_module()

    except:
        print('Error while testing ShadowSuiteLE class list_module method...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Testing ShadowSuiteLE class find_module method with the valid keyword \'sample\'...')
        print()
        API.ShadowSuiteLE().find_module('sample')

    except:
        print('Error while testing ShadowSuiteLE class find_module method...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Testing ShadowSuiteLE class find_module with the invalid keyword \'njsk2468\'...')
        print()
        API.ShadowSuiteLE().find_module('njsk2468')

    except:
        print('Error while testing ShadowSuiteLE class find_module method...')
        traceback.print_exc()
        sys.exit(1)
        
    try:
        print('Testing ShadowSuiteLE class use_module method with the valid keyword \'sample\'...')
        print()
        API.ShadowSuiteLE().use_module('sample')
    
    except:
        print('Error while testing ShadowSuiteLE class use_module method...')
        traceback.print_exc()
        sys.exit(1)
        
    try:
        print('Testing ShadowSuiteLE class use_module with the invalid keyword \'njsk2468\'...')
        print()
        API.ShadowSuiteLE().use_module('njsk2468')
    
    except:
        print('Error while testing ShadowSuiteLE class use_module method...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Testing ShadowSuiteLE class suggest method with the valid keyword \'reconnaissance\'...')
        print()
        API.ShadowSuiteLE().suggest('reconnaissance')

    except:
        print('Error while testing ShadowSuiteLE class suggest method...')
        traceback.print_exc()
        syd.exit(1)

    try:
        print('Testing ShadowSuiteLE class pause method...')
        print()
        API.ShadowSuiteLE().pause()

    except:
        print('Error while testing ShadowSuiteLE class pause method...')
        traceback.print_exc()
        sys.exit(1)

    try:
        print('Testing ShadowSuiteLE class clrscrn method...')
        print()
        API.ShadowSuiteLE().clrscrn()

    except:
        print('Error while testing ShadowSuiteLE class clrscrn method...')
        traceback.print_exc()
        sys.exit(1)

    print('Finished testing API!')

if __name__ == '__main__':
    main()
