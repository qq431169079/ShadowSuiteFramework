#!/usr/bin/env python

import base64
from core import misc

def caesar(plainText, shift):
    cipherText = ""
    for ch in plainText.lower():
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26

            finalLetter = chr(stayInAlphabet)

        else:
            finalLetter = ch

        cipherText += finalLetter

    return cipherText

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
    masc_table = {'a': 'n',
                'b': 'o',
                'c': 'a',
                'd': 't',
                'e': 'r',
                'f': 'b',
                'g': 'e',
                'h': 'c',
                'i': 'f',
                'j': 'u',
                'k': 'x',
                'l': 'd',
                'm': 'q',
                'n': 'g',
                'o': 'y',
                'p': 'l',
                'q': 'k',
                'r': 'h',
                's': 'v',
                't': 'i',
                'u': 'j',
                'v': 'm',
                'w': 'p',
                'x': 'z',
                'y': 's',
                'z': 'w'}

    for char in msg:
        if char in masc_table:
            new_char = masc_table[char]
            result += new_char

        else:
            result += char

    return result

def base64e(msg):
    result = base64.b64encode(msg)
    return result

def leet(msg):
    msg = msg.lower()
    result = ""
    masc_table = {'a': '@',
                'c': '(',
                'e': '3',
                'i': '!',
                'l': '1',
                'o': '0',
                'q': '9',
                'r': '6',
                's': '5',
                't': '7',}

    for char in msg:
        if char in masc_table:
            new_char = masc_table[char]
            result += new_char

        else:
            result += char

    return result
