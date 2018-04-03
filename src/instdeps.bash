#!/data/data/com.termux/files/usr/bin/bash
# Coding=UTF-8

# Install packages listed in apt_requirements file.

xargs -0 apt install -y --upgrade < <(tr \\n \\0 < apt_requirements)
