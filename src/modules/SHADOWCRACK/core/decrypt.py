#!/usr/bin/env python

import base64
from core import misc

def caesar(cipherText, shift):
    plainText = ""
    for ch in cipherText.lower():
        if ch.isalpha():
            stayInAlphabet = ord(ch) - shift
            if stayInAlphabet < ord('a'):
                stayInAlphabet += 26

            finalLetter = chr(stayInAlphabet)

        else:
            finalLetter = ch

        plainText += finalLetter

    return plainText

def reverse(msg):
    msg = str(msg.lower())
    step1 = []
    result = ""
    for char in msg:
        step1.append(char)

    step2 = step1[::-1]
    for last in step2:
        result = result + last

    return result

def atbash(msg):
    msg = str(msg.lower())
    result = ""
    atbash_table = {'a': 'z',
                    'b': 'y',
                    'c': 'x',
                    'd': 'w',
                    'e': 'v',
                    'f': 'u',
                    'g': 't',
                    'h': 's',
                    'i': 'r',
                    'j': 'q',
                    'k': 'p',
                    'l': 'o',
                    'm': 'n',
                    'n': 'm',
                    'o': 'l',
                    'p': 'k',
                    'q': 'j',
                    'r': 'i',
                    's': 'h',
                    't': 'g',
                    'u': 'f',
                    'v': 'e',
                    'w': 'd',
                    'x': 'c',
                    'y': 'b',
                    'z': 'a'}

    for char in msg:
        if char in atbash_table:
            new_char = atbash_table[char]
            result += new_char

        else:
            result += char

    return result

def masc(msg):
    msg = str(msg.lower())
    result = ""
    masc_table = {'n': 'a',
                'o': 'b',
                'a': 'c',
                't': 'd',
                'r': 'e',
                'b': 'f',
                'e': 'g',
                'c': 'h',
                'f': 'i',
                'u': 'j',
                'x': 'k',
                'd': 'l',
                'q': 'm',
                'g': 'n',
                'y': 'o',
                'l': 'p',
                'k': 'q',
                'h': 'r',
                'v': 's',
                'i': 't',
                'j': 'u',
                'm': 'v',
                'p': 'w',
                'z': 'x',
                's': 'y',
                'w': 'z'}

    for char in msg:
        if char in masc_table:
            new_char = masc_table[char]
            result += new_char

        else:
            result += char

    return result

def base64d(msg):
    result = base64.b64decode(msg)
    result = result.decode()
    return result

def leet(msg):
    msg = msg.lower()
    result = ""
    masc_table = {'@': 'a',
                '(': 'c',
                '3': 'e',
                '!': 'i',
                '1': 'l',
                '0': 'o',
                '9': 'q',
                '6': 'r',
                '5': 's',
                '7': 't',}

    for char in msg:
        if char in masc_table:
            new_char = masc_table[char]
            result += new_char

        else:
            result += char

    return result
