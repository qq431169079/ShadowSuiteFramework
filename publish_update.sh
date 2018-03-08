#!/usr/bin/bash

echo "Enter version:"
read VERSION
echo ""
echo "[i] Now publishing update..."
echo ""
git status
echo "[!] Press any key to continue..."
read TEMP
git clean -dfi
echo "[!] Press any key to continue..."
read TEMP
git gc
echo "[!] Press any key to continue..."
read TEMP
git add .
echo "[!] Press any key to continue..."
read TEMP
git commit -as
echo "[!] Press any key to continue..."
read TEMP
git status
echo "[!] Press any key to continue..."
read TEMP
git gc
echo "[!] Press any key to continue..."
read TEMP
git tag $VERSION
echo "[!] Press any key to continue..."
read TEMP
git tag
echo "[!] Press any key to continue..."
read TEMP
git log
echo "[!] Press any key to continue..."
read TEMP
git status
echo "[!] Press any key to continue..."
read TEMP
git push
echo "[i] Update $VERSION published..."
