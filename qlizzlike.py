# Scripted By Mr_Dark 2022
# ingatlah bahwa aldo itu gay -_-



import requests,time,random,string,sys

# cookie nya ga w masukkin karena udh di tambah ke dalam save session


headers = {
    'authority': 'instagram.qlizz.com',
    'accept': '*/*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.684540350.1652173099; _gid=GA1.2.1932374052.1652173099; _gat_gtag_UA_137153197_1=1; __gads=ID=5a201913cb3adcd6-2285e36d20d300f8:T=1652173100:RT=1652173100:S=ALNI_Ma5T99MHBxaAI7ZNxZzKkvhw13pcg; XSRF-TOKEN=eyJpdiI6IitcL21FZlU1XC82WXBRQ1E0ZlNXY0lydz09IiwidmFsdWUiOiJYTm82MGFXQWhHZ1UxQmZZZXI3VTdaQ0syalRhZ3ZEcFVUenI5TmVpTTl6VWMyZHpmNWtFZFlWWWhXVGN2SVlMdFZBR2UwRmcwYnRHeDJhaWxqK045QT09IiwibWFjIjoiZWM1ZjRjMTBlNDQ0NGU3NjgzN2FmMDA1ZTg5NjJiMjBmNTlmMjQ0MDFlNTBlODIxMTkwNGVjYTY5NTk1YTlhMSJ9; laravel_session=eyJpdiI6InNUXC9HUDlQUXdcL3lBdmFQTktWNWJVQT09IiwidmFsdWUiOiI1VEx5T29GR04zZVwvOUlzUVR1T3ZVbG5iK1FQWXcxYlR4ZHhwNkpoK2hzSXRPcEN1c1o3ZWk0SUVKcHpjcGd4bXRnSWVReU1qUURCcG8wUVd1ejA4VGc9PSIsIm1hYyI6ImZkOGNiNmVmNDBkYTFkN2Q4MmY1YmQ1NDFkYTEzMmE5ZWUwNWNmNWQ3NWU2MmU4ODVlZWI5MThmMmVhYjg4M2IifQ%3D%3D',
    'origin': 'https://instagram.qlizz.com',
    'referer': 'https://instagram.qlizz.com/autofollowers',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
    'x-requested-with': 'XMLHttpRequest',
}
perdigay = random.choice(string.ascii_letters)
perdigaay = random.choice(string.ascii_letters)
perdigaa = random.choice(string.ascii_letters)
#user = input("username akun tumbal\ninput> ")
#passw = input("password akun tumbal\ninput> ")
user = f"{perdigaa}subscribe_mrdark_{perdigaay}{perdigay}"
passw = f"a{perdigaa}j{perdigaay}wnjn{perdigay}"
#XenziGay = input("username yang ingin di tambah follower nya, tanpa @\ninput> ")
XenziGay = sys.argv[1];
#time.sleep(2)
bruh = {
    'username': user,
    'password': passw,
}
s = requests.Session()
s.post('https://instagram.qlizz.com/login', data=bruh)
alok = s.get('https://instagram.qlizz.com/autoliker').text
#print (alok)
a = alok.split('name="_token" value="')[1];
tok = a.split('"')[0];
print ("*set hidden token:* _"+tok+"_")
print ("*set fake username:* _"+user+"_")
print ("*set fake password:* _"+passw+"_")
data = {
    '_token': tok,
    'link': XenziGay,
    'tool': 'autoliker',
}

response = s.post('https://instagram.qlizz.com/send', headers=headers, data=data).text
print ("*Your response code:* _"+response+"_")