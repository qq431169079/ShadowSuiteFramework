#!/usr/bin/bash

echo "Enter version:"
read VERSION
echo ""
echo "[i] Now publishing update..."
echo ""
git status
git gc
read TEMP
git add .
git commit -as
git status
read TEMP
git gc
read TEMP
git tag $VERSION
git tag
read TEMP
git log
read TEMP
git status
read TEMP
git push
