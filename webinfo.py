import requests, sys, shlex
drak = sys.argv[1];
params = {
    'host': drak,
}

response = requests.get('https://check-host.net/ip-info', params=params).text
a = response.split("<td>")[32];
b = a.split("</td>")[0];
a = response.split("<td>")[34];
org = a.split("</td>")[0];
a = response.split("<strong>")[9];
id = a.split("</strong>")[0];
a = response.split("<td>")[4];
host = a.split("</td>")[0];
a = response.split("<td>")[38];
daerah = a.split("</td>")[0];
print (f"""
-----------------
© DarkBotMD 2022
-----------------
ISP: {b}
Organization: {org}
Hostname: {host}
Country: {id}
Region: {daerah}
""")
