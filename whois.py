import requests, sys
domain = sys.argv[1].replace('http://','').replace('https://','')
cookies = {
    '__utmz': '176354173.1660363776.1.1.utmccn=(referral)|utmcsr=bing.com|utmcct=/|utmcmd=referral',
    '__utma': '176354173.399594685.1660363776.1661061477.1661392278.8',
    '__utmb': '176354173',
    '__utmc': '176354173',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '__utmz=176354173.1660363776.1.1.utmccn=(referral)|utmcsr=bing.com|utmcct=/|utmcmd=referral; __utma=176354173.399594685.1660363776.1661061477.1661392278.8; __utmb=176354173; __utmc=176354173',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(f'https://intodns.com/{domain}', cookies=cookies, headers=headers).text
if '<td>Domain NS records</td>' in response:
	print (f"Domain NameServer Record 1 is: {response.split('<br />')[2].split('.&')[0]}\nDomain NameServer Record 2 is: {response.split('<br />')[3].split('.&')[0]}")
else:
	print ("there was an unexpected error with IntoDNS")