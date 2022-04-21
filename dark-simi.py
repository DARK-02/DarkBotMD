import os,sys,requests,shlex
from requests import get
mr_dark = " ".join(map(shlex.quote, sys.argv[1:]))
#mr_dark_url = f'https://api.simsimi.net/v2/?text={mr_dark}&lc=id'
#dark = requests.get(mr_dark_url)
cookies = {
    '_ga': 'GA1.1.666863305.1650578072',
    '_ga_L8BJYNG33X': 'GS1.1.1650578072.1.0.1650578072.0',
    'PHPSESSID': 'a0785e719917ca2355a1260ca60746c9',
}

headers = {
    'authority': 'simsimi.info',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.1.666863305.1650578072; _ga_L8BJYNG33X=GS1.1.1650578072.1.0.1650578072.0; PHPSESSID=a0785e719917ca2355a1260ca60746c9',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
}

params = {
    'text': mr_dark,
    'lc': 'id',
}

dark = requests.get('https://simsimi.info/api/', headers=headers, params=params, cookies=cookies)
if dark.status_code == 200:
     print('_simi bot_: ', dark.json().get('success'))
     print('ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ ᴍʀ_ᴅᴀʀᴋ')
else:
     print('bad respon ')
