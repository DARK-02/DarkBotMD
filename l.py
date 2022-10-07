import requests

cookies = {
    'XSRF-TOKEN': '12D59ACD8AA0B88A7ACE05BB574FAF8955D23DBA28E8EE54F30BCB106413A89C1752BA30DC063940ED30A599C055CC810636',
    '_gcl_au': '1.1.1860823839.1661903409',
    '_ga': 'GA1.2.508329863.1661903409',
    '_gid': 'GA1.2.1184679397.1661903409',
    'ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7': '%7B%22g%22%3A%2218bb4559-2170-9c14-ddcd-2dc80d13c3e3%22%2C%22c%22%3A1656491802961%2C%22l%22%3A1661903408779%7D',
    'afUserId': '52293775-f4c9-4ce2-9002-5137c5a1ed24-p',
    'AF_SYNC': '1661903410542',
    'amp_394863': 'nZm2vDUbDAvSia6NQPaGum...1gboij3ii.1gboijph0.3.0.3',
    'ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7': '%7B%22g%22%3A%22b35e0302-0684-1962-c1a1-86e8350b6be4%22%2C%22e%22%3A1661905231205%2C%22c%22%3A1661903408777%2C%22l%22%3A1661903431205%7D',
}

headers = {
    'authority': 'www.halodoc.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'XSRF-TOKEN=12D59ACD8AA0B88A7ACE05BB574FAF8955D23DBA28E8EE54F30BCB106413A89C1752BA30DC063940ED30A599C055CC810636; _gcl_au=1.1.1860823839.1661903409; _ga=GA1.2.508329863.1661903409; _gid=GA1.2.1184679397.1661903409; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%2218bb4559-2170-9c14-ddcd-2dc80d13c3e3%22%2C%22c%22%3A1656491802961%2C%22l%22%3A1661903408779%7D; afUserId=52293775-f4c9-4ce2-9002-5137c5a1ed24-p; AF_SYNC=1661903410542; amp_394863=nZm2vDUbDAvSia6NQPaGum...1gboij3ii.1gboijph0.3.0.3; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7=%7B%22g%22%3A%22b35e0302-0684-1962-c1a1-86e8350b6be4%22%2C%22e%22%3A1661905231205%2C%22c%22%3A1661903408777%2C%22l%22%3A1661903431205%7D',
    'origin': 'https://www.halodoc.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    'x-xsrf-token': '12D59ACD8AA0B88A7ACE05BB574FAF8955D23DBA28E8EE54F30BCB106413A89C1752BA30DC063940ED30A599C055CC810636',
}
nomor = input("nomor: ")
json_data = {
    'phone_number': '+62'+nomor,
    'channel': 'voice',
}

response = requests.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', cookies=cookies, headers=headers, json=json_data).text
print (response)