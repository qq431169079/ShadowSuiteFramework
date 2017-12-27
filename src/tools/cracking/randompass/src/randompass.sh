#!/bin/bash

# Random password generator
# Not as secure as others.

# Install dependencies
apt install pwgen
apt install vim
apt install figlet

# Program Start
clear
figlet Pwgen
figlet -f mini Password Generator
figlet -f mini Version 1.0
echo ""
echo "Press any key to generate a block of password..."
read startit
echo "Please copy the password block below:" >> generated.txt
echo "-----------------------------------------" >> generated.txt
# Password block generation
pwgen -c -n -y -s -C >> generated.txt
echo "" >> generated.txt
echo "" >> generated.txt
echo "Type ':q!' or press the escape button and type ':q!' to quit." >> generated.txt
echo ""
echo "Successfully generated a random password!"
echo "Press any key to open the file..."
echo "When the file is opened, please copy the contents..."
read endit
clear
# Opens the generated password block and deletes it after opening.
vim generated.txt
rm generated.txt
exit 0
