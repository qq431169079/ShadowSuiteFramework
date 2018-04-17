#!/bin/python
# Coding=UTF-8

import os
import sys
import traceback

banner = r""" ____  _               _                ____                _    _
/ ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | _| |
\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |   | '__/ _` |/ __| |/ / |
 ___) | | | | (_| | (_| | (_) \ V  V /| |___| | | (_| | (__|   <|_|
|____/|_| |_|\__,_|\__,_|\___/ \_/\_/  \____|_|  \__,_|\___|_|\_(_) """

help = r"""               COMMAND    ::    DESCRIPTION

               help       ::    prints this help menu.
               encrypt    ::    encrypt a string.
               decrypt    ::    decrypt a ciphertext.
               info       ::    shows info about an algorithm.
               clear      ::    clears the contents of the screen.

               quit       ::    exit Shadow Crack."""

ciphers = r"""                Easy Algorithms (Low security)
                [01] Caesar Code (Substitution)
                [02] Reverse Code (Tranposition/Words)
                [03] Atbash / Basic Substitution Cipher (Substitution)
                [04] Mono-Alphabetic Substitution Cipher (Substitution)
                [05] Base64 (Substitution)
                [06] 1337 mode (Substitution)
                [07] Date-Shift Cipher (Transposition)
                [08] Reflect Method (Substitution)
                [09] Basic Transposition Cipher (Transposition)
                [10] Double Transposition Cipher (Transposition)
                [11] ShadowCrypt (Substitution)

                Medium Algorithms (Medium Security)
                [12] Binary Code (Numbers)
                [13] ASCII Code (Numbers)
                [14] Morse Code (Transposition/Words)
                [15] Hexadecimal Code (Numbers)
                [16] Combined Approach (Transposition)
                [17] XOR Toy Cipher (Stream)
                [18] Chaffing Algorithm (N/A)

                Complex Algorithms (High Security)
                [19] Vigenere Code (Substitution)
                [20] AES (Symmetric Key)
                [21] RSA (Asymmetric Key)
                [22] SCA (Cipher Combinations)
                [23] RC2 (Symmetric Key)
                [24] ARC4 (Symmetric Key)
                [25] Blowfish (Symmetric Key)
                [26] CAST-128/CAST5 (Symmetric Key)
                [27] DES (Symmetric Key)
                [28] Triple DES/DES3 (Symmetric Key)
                [29] RSAES-OAEP (N/A)
                [30] RSAES-PKCS1-v1_5 (N/A)
                [31] All or Nothing Algorithm (Package Transformation)
                [32] KDF/Standard Key Derivation Function (N/A)
                [33] DSA (Public-Key Signature)
                [34] ElGamal (Public-Key Signature)

                One-Way Algorithms (Higher Security)
                [35] MD2 Algorithm (Hash)
                [36] MD4 Algorithm (Hash)
                [37] MD5 Algorithm (Hash)
                [38] SHA-1 Algorithm (Hash)
                [39] SHA-224 Algorithm (Hash)
                [40] SHA-256 Algorithm (Hash)
                [41] SHA-384 Algorithm (Hash)
                [42] SHA-512 Algorithm (Hash)
                [43] HMAC Algorithm (Hash)
                [44] RIPEMD-160 (Hash)"""

invalid_input = "Invalid Input!"

coming_soon = "Feature Coming soon!"

copyright = "Copyright(C) 2018 by Shadow Team"

letters_only = "Sorry! The message must contain letters only!"

class unixColors():
    # Colors
    cw = '\033[0m'     #  white
    cr = '\033[31m'    #  red
    cg = '\033[32m'    #  green
    cy = '\033[33m'    #  yellow
    cb = '\033[34m'    #  blue
    cgr = '\033[37m'   #  gray
    cp = '\033[35m'    #  purple
    cc = '\033[36m'    #  cyan

class unixFonts():
    fr = '\033[0m'     #  regular
    fb = '\033[1m'     #  bold
    fi = '\033[3m'     #  italic

class programFunctions():
    def program_restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

    def clrscrn(self):
        platform = sys.platform
        if platform == 'linux':
            os.system('clear')

        elif platform == 'windows':
            os.system('cls')

        else:
            os.system('clear')

    def pause(self, silent=False):
        platform = sys.platform
        if platform == 'linux':
            if silent is False:
                print('Press any key to continue...')
                os.system('read A972681B318C92911A4020C18ACF78B6')

            else:
                os.system('read A972681B318C92911A4020C18ACF78B6')

        elif platform == 'windows':
            if silent is False:
                os.system('pause')

            else:
                os.sysem('pause > nul')

        else:
            if silent is False:
                print('Press any key to continue...')
                os.system('read A972681B318C92911A4020C18ACF78B6')

            else:
                os.system('read A972681B318C92911A4020C18ACF78B6')
