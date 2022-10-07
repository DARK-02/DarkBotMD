import requests,sys,shlex
mr_dark = " ".join(map(shlex.quote, sys.argv[1:]))
headers = {
    'Accept': '*/*',
    'Accept-Language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://pikwy.com',
    'Referer': 'https://pikwy.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'tkn': '125',
    'd': '3000',
    'u': mr_dark,
    'fs': '0',
    'w': '1280',
    'h': '1200',
    's': '100',
    'z': '100',
    'f': 'jpg',
    'rt': 'jweb',
}

response = requests.get('https://api.pikwy.com/', params=params, headers=headers).text
a = response.split('"iurl":"')[1];
b = a.split('"')[0];
print ('url screenshot: '+b)