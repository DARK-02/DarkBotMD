
import requests, sys
p = sys.argv[1]
import requests

cookies = {
    '_pbjs_userid_consent_data': '6683316680106290',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    '_ga': 'GA1.2.815795347.1661402718',
    '_gid': 'GA1.2.1769607613.1661402718',
    '_gat_gtag_UA_58443135_1': '1',
    'cto_bundle': 'w4qC2V9BOFJ2dndES0s1TWRUekJlViUyQkJ3JTJCQjA2SU9zOW4ybzRqRlNYTnR2aDhTWm56TGxSaWs2emZYTWdKeTFScHB4JTJGTkIlMkJwSUNtUlQ5QnM4VG8ySzAyejlmbzRCMGs3ZlpkTm9oSkNkRTJ4JTJCN2ZURjJlM0xaSTJjR2I5c00xaGpWWFFYVDdxNzNra29YVHVTYnhhZ1h1MiUyRnclM0QlM0Q',
    'cto_bidid': 'wL9QNF9DN1dWdkslMkJpU2lFRSUyQnh2RDBkNXhCeUxkRUdpWGdJdjM0YnlKT3hwdjNhZkZuelJIQTJGJTJGcEFKUFB2QWN6SEZKVExvaUl4eGdGZ0dvWE95SmhUUkVVaCUyQnZzZWM0ZklVVjdhdnhQR3E2N2t3JTNE',
    'cto_bundle': 'jIml-19BOFJ2dndES0s1TWRUekJlViUyQkJ3JTJCTzdVa0VveU50OGFxT1o2ZFBoZjE0YUM4UXJBMWxGV3ZHS09rRmVrQWJYRG9WJTJGJTJCcG1uZTQlMkZ1bDZHMTk4UTN4RXdNQnRmeGlURmc3JTJGVGN0clJoZk5BWSUyQjl5b3M3UE45YlY2OCUyRmozeWFmdGZzanhuN1p1dURwYUtIdFNVS3kzQ3JRJTNEJTNE',
    '__gads': 'ID=7f573b655656d0b7:T=1661402722:S=ALNI_MaixH55QHPtZCkbCx0EQgERl9bG9Q',
    '__gpi': 'UID=0000090362bc3416:T=1661402722:RT=1661402722:S=ALNI_MY8RB8idumG03DyLKMIv1XW_YExdg',
    '_cc_id': '8699913a7e9ff6badb25b61016378001',
    'panoramaId_expiry': '1662007523254',
    'panoramaId': '5fef3ed1bcbb4fea7e5c9a3939be16d53938838776f76d551876e34600cd5cae',
}

headers = {
    'authority': 'geekflare.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_pbjs_userid_consent_data=6683316680106290; _lr_retry_request=true; _lr_env_src_ats=false; _ga=GA1.2.815795347.1661402718; _gid=GA1.2.1769607613.1661402718; _gat_gtag_UA_58443135_1=1; cto_bundle=w4qC2V9BOFJ2dndES0s1TWRUekJlViUyQkJ3JTJCQjA2SU9zOW4ybzRqRlNYTnR2aDhTWm56TGxSaWs2emZYTWdKeTFScHB4JTJGTkIlMkJwSUNtUlQ5QnM4VG8ySzAyejlmbzRCMGs3ZlpkTm9oSkNkRTJ4JTJCN2ZURjJlM0xaSTJjR2I5c00xaGpWWFFYVDdxNzNra29YVHVTYnhhZ1h1MiUyRnclM0QlM0Q; cto_bidid=wL9QNF9DN1dWdkslMkJpU2lFRSUyQnh2RDBkNXhCeUxkRUdpWGdJdjM0YnlKT3hwdjNhZkZuelJIQTJGJTJGcEFKUFB2QWN6SEZKVExvaUl4eGdGZ0dvWE95SmhUUkVVaCUyQnZzZWM0ZklVVjdhdnhQR3E2N2t3JTNE; cto_bundle=jIml-19BOFJ2dndES0s1TWRUekJlViUyQkJ3JTJCTzdVa0VveU50OGFxT1o2ZFBoZjE0YUM4UXJBMWxGV3ZHS09rRmVrQWJYRG9WJTJGJTJCcG1uZTQlMkZ1bDZHMTk4UTN4RXdNQnRmeGlURmc3JTJGVGN0clJoZk5BWSUyQjl5b3M3UE45YlY2OCUyRmozeWFmdGZzanhuN1p1dURwYUtIdFNVS3kzQ3JRJTNEJTNE; __gads=ID=7f573b655656d0b7:T=1661402722:S=ALNI_MaixH55QHPtZCkbCx0EQgERl9bG9Q; __gpi=UID=0000090362bc3416:T=1661402722:RT=1661402722:S=ALNI_MY8RB8idumG03DyLKMIv1XW_YExdg; _cc_id=8699913a7e9ff6badb25b61016378001; panoramaId_expiry=1662007523254; panoramaId=5fef3ed1bcbb4fea7e5c9a3939be16d53938838776f76d551876e34600cd5cae',
    'origin': 'https://geekflare.com',
    'referer': 'https://geekflare.com/tools/isitdown',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
}

json_data = {
    'url': p,
    'type': 'isitdown',
    'locations': [
        'us',
        'uk',
        'sg',
    ],
}

response = requests.post('https://geekflare.com/tools/api/up', headers=headers, json=json_data).text
if response == 'Site is down':
	stat =" *WEBSITE DOWN*!"
else:
	stat = "*WEBSITE IS UP*"
print (f"\t[{p}]\n{stat}\nRaw response: {response}")
