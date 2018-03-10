#!/usr/bin/bash

echo "Enter version:"
read VERSION
echo ""
echo "[i] Now publishing update... (Git status)"
echo ""
git status
echo "[!] Press any key to continue... (Git clean -dfi)"
read TEMP
git clean -dfi
echo "[!] Press any key to continue... (Git gc)"
read TEMP
git gc
echo "[!] Press any key to continue... (Git add .)"
read TEMP
git add .
echo "[!] Press any key to continue... (Git comit -as)"
read TEMP
git commit -as
echo "[!] Press any key to continue... (Git status)"
read TEMP
git status
echo "[!] Press any key to continue... (Git gc)"
read TEMP
git gc
echo "[!] Press any key to continue... (Git tag)"
read TEMP
git tag $VERSION
echo "[!] Press any key to continue... (Git tag)"
read TEMP
git tag
echo "[!] Press any key to continue... (Git log)"
read TEMP
git log
echo "[!] Press any key to continue... (Git status)"
read TEMP
git status
echo "[!] Press any key to continue... (Git push)"
read TEMP
git push
echo "[i] Update $VERSION published..."
