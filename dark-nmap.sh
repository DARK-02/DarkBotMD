echo "© Mr_Dark 2022" && echo "Starting Dark-Nmap 7.40 ( DarkNmap )"
curl https://hackertarget.com/nmap-online-port-scanner/ --data "theinput="$1"&thetest=nmap&name_of_nonce_field=945655f3c3&_wp_http_referer=%2Fnmap-online-port-scanner%2F" 2>&1 | grep -Pzo "Host is up.(.|\n)*\nNmap done"
