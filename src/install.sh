#!bin/bash

echo "Compiling..."
cc -o hackers *.c
echo "Compiling... Done!"
echo "Press any key to test the program..."
read temporary
ShadowFramework
