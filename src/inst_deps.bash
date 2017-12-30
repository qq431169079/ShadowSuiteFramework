#!/data/data/com.termux/files/usr/bin/bash

xargs -0 apt install -y < <(tr \\n \\0 < apt_requirements)
