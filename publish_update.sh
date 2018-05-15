#!/usr/bin/env bash

echo "Edit version on README.md and version.py... (vim README.md src/core/version.py)"
read TEMP
vim README.md src/core/version.py
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
echo "[!] Press any key to continue... (staging and unstaging)"
read TEMP
tig status
echo "[!] Press any key to continue... (Git commit -s)"
read TEMP
git commit -s
echo "[!] Press any key to continue... (Git status)"
read TEMP
git status
echo "[!] Press any key to continue... (Git gc)"
read TEMP
git gc
echo "[!] Press any key to continue... (Git tag)"
read TEMP
git tag $VERSION
echo "[!] Press any key to continue... (Git log)"
read TEMP
git log
cd src/extras/
git log > changelog
cd ../..
echo "[!] Press any key to continue... (Git commit -s)"
read TEMP
git add src/extras/changelog
git commit -s -m 'Added changelog.'
echo "[!] Press any key to continue... (Git status)"
read TEMP
git status
echo "[!] Press any key to continue... (Git push)"
read TEMP
git push
echo "[i] Update $VERSION published..."
