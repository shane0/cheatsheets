#!/usr/bin/env bash

echo "# cheatsheets" >> readme.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:shane0/cheatsheets.git
git push -u origin main