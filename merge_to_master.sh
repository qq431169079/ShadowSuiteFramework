#!/usr/bin/bash

git branch
echo "Enter your current branch:"
read BRANCH
echo "Enter version:"
read VERSION
echo ""
echo "[i] Merging to master branch..."
echo ""
git status
git gc
read TEMP
git add .
git commit -as
git status
read TEMP
git checkout master
git status
read TEMP
git merge $BRANCH
git status
read TEMP
git gc
read TEMP
git tag
git log
read TEMP
git checkout $BRANCH
git status
