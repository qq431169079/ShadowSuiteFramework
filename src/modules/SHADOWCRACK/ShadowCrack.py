#!/usr/bin/env python

# Import directives
try:
    import os
    import sys
    import traceback

    import base64

    from core import misc
    from core import encrypt
    from core import decrypt
    # from core import info # DEV0001

except ImportError:
    # Prints if error is encountered while importing modules.
    print("Import Error!")
    print()
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")

def main(): # The Main Function
    print(misc.banner)
    print('\n' + misc.copyright)
    print('\n\n')
    while True:
        try:
            command = str(input(" >>> "))
            command = command.lower()
        
            if command == 'help':
                print(misc.help)
        
            elif command == 'encrypt':
                print(misc.ciphers)
                try:
                    cipher = int(input(' >>> '))
                    
                    if cipher == 1:
                        print("[i] Ceasar cipher automatically disables capitalization.")
                        caesar_msg = str(input("Message: "))
                        caesar_shift = int(input("Shift: "))
                        result = encrypt.caesar(caesar_msg, caesar_shift)
                        print(result)
                        misc.programFunctions().pause()
                        del caesar_msg
                        del caesar_shift
                        del result

                    elif cipher == 2:
                        reverse_msg = str(input("Message: "))
                        result = encrypt.reverse(reverse_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del reverse_msg
                        del result

                    elif cipher == 3:
                        atbash_msg = str(input("Message: "))
                        result = encrypt.atbash(atbash_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del atbash_msg
                        del result

                    elif cipher == 4:
                        masc_msg = str(input("Message: "))
                        result = encrypt.masc(masc_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del masc_msg
                        del result

                    elif cipher == 5:
                        ### DEV0001 Base64 decoder and encoder isn't working! ###
                        base64_msg = str(input("Message: ")).encode()
                        result = str(encrypt.base64e(base64_msg))
                        result = result.replace("b'", '')
                        result = result.replace("'", '')
                        print(result)
                        misc.programFunctions().pause()
                        del base64_msg
                        del result

                    elif cipher == 6:
                        leet_msg = str(input("Message: "))
                        result = encrypt.leet(leet_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del leet_msg
                        del result

                    else:
                        print(misc.invalid_input)

                except Exception as e:
                    print(e)
                    print()
                    traceback.print_exc()

                except KeyboardInterrupt:
                    print("CTRL+C Detected, now quitting...")
                    sys.exit(1)

            elif command == 'decrypt':
                print(misc.ciphers)
                try:
                    cipher = int(input(' >>> '))

                    if cipher == 1:
                        print("[i] Ceasar cipher automatically disables capitalization.")
                        caesar_ciphertext = str(input("Ciphertext: "))
                        caesar_shift = int(input("Number of rotations: "))
                        result = decrypt.caesar(caesar_ciphertext, caesar_shift)
                        print(result)
                        misc.programFunctions().pause()
                        del caesar_ciphertext
                        del caesar_shift
                        del result

                    elif cipher == 2:
                        reverse_msg = str(input("Message: "))
                        result = decrypt.reverse(reverse_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del reverse_msg
                        del result

                    elif cipher == 3:
                        atbash_msg = str(input("Message: "))
                        result = decrypt.atbash(atbash_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del atbash_msg
                        del result

                    elif cipher == 4:
                        masc_msg = str(input("Message: "))
                        result = decrypt.masc(masc_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del masc_msg
                        del result

                    elif cipher == 5:
                        base64_msg = str(input("Message: "))
                        result = decrypt.base64d(base64_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del base64_msg
                        del result

                    elif cipher == 6:
                        leet_msg = str(input("Message: "))
                        result = decrypt.leet(leet_msg)
                        print(result)
                        misc.programFunctions().pause()
                        del leet_msg
                        del result

                    else:
                        print(misc.invalid_input)

                except Exception as e:
                    print(e)
                    print()
                    traceback.print_exc()

            elif command == 'info':
                print(misc.coming_soon)

            elif command == "clear":
                misc.programFunctions().clrscrn()

            elif command == 'quit':
                exit(0)

            else:
                print(misc.invalid_input)
        
        except KeyboardInterrupt:
            print("CTRL+C detected, quitting...")
            sys.exit(1)

        except Exception as e:
            print(e)
            print()
            traceback.print_exc()

# If running independently, run main() function.
if __name__ == '__main__':
    main()
    sys.exit(0)
