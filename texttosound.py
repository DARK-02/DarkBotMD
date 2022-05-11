import requests,os,sys,shlex
PerdiHalu = " ".join(map(shlex.quote, sys.argv[1:]))

cookies = {
    '_ga': 'GA1.2.59392139.1652070996',
    '_gid': 'GA1.2.1183941107.1652070996',
    '__gads': 'ID=a64836eec2a0b6ab-228dcd301ad300ad:T=1652070996:RT=1652070996:S=ALNI_MZsRZS5nz_oSFSdFCT5WHwfnnz5nA',
}

headers = {
    'authority': 'freetts.com',
    'accept': '*/*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.59392139.1652070996; _gid=GA1.2.1183941107.1652070996; __gads=ID=a64836eec2a0b6ab-228dcd301ad300ad:T=1652070996:RT=1652070996:S=ALNI_MZsRZS5nz_oSFSdFCT5WHwfnnz5nA',
    'referer': 'https://freetts.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
    'x-requested-with': 'XMLHttpRequest',
}

perdi = {
    'Language': 'id-ID',
    'Voice': 'id-ID-Standard-C',
    'TextMessage': PerdiHalu,
    'type': '0',
}

response = requests.get('https://freetts.com/Home/PlayAudio', params=perdi).text
dark = response.split('id":"')[1];
drak = dark.split('"')[0];
alok = requests.get(f"https://freetts.com/audio/{drak}")
os.system("rm p.mp3")
os.system(f"curl --silent --url 'https://freetts.com/audio/{drak}' > p.mp3")
