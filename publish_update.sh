#!/usr/bin/bash

echo "Enter version:"
read VERSION
echo ""
echo "[i] Now publishing update..."
echo ""
git status
read TEMP
git clean -dfi
read TEMP
git gc
read TEMP
git add .
read TEMP
git commit -as
read TEMP
git status
read TEMP
git gc
read TEMP
git tag $VERSION
read TEMP
git tag
read TEMP
git log
read TEMP
git status
read TEMP
git push
echo "[i] Update \'$VERSION\' published..."
