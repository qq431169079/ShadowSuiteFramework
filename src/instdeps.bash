#!/data/data/com.termux/files/usr/bin/bash

# Install packages listed in apt_requirements file.

xargs -0 apt install -y < <(tr \\n \\0 < apt_requirements)
