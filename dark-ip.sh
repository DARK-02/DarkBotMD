echo "_© Mr_Dark 2022_"
echo "----Host----"
echo $1
#nmap = curl https://hackertarget.com/nmap-online-port-scanner/ --data "theinput="$1"&thetest=nmap&name_of_nonce_field=945655f3c3&_wp_http_referer=%2Fnmap-online-port-scanner%2F" 2>&1 | grep -Pzo "Host is up.(.|\n)*\nNmap done"
echo "-----IP-----"
curl --silent https://url-decode.com/tools_files/hostname-to-ip/hostname_to_ip_ajax.php --data 'host='$1'' | tr -d '"' | tr -d 'success' | tr -d '{' | tr -d ':' | tr -d '}' && echo ''
echo "------------"
