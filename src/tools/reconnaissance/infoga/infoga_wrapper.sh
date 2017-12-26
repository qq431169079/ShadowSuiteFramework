#!/data/data/com.termux/files/usr/bin/bash

echo ""
echo "Enter the domain to search:"
read TARGET
echo ""
echo "Running..."
echo ""
echo ""
echo ""
python2 infoga.py --target $TARGET --source all --verbose
echo ""
echo ""
echo ""
echo "Running... Done!"
read waitforexit
exit 0
