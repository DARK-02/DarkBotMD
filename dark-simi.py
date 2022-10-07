import os,sys,requests,shlex,random,re
from datetime import datetime
from datetime import date
from requests import get
mr_dark = " ".join(map(shlex.quote, sys.argv[1:]))
#gboleh = "D" and "R" and "K" and "G" and "A" and "Y","I","4"
#word = str(mr_dark)
if re.findall('^.*[dD].*[rR].*[kK].*[gG].*[3eEaA4].*[yYi1I]', mr_dark):
	print(f'_simi bot_: {random.choice(["ndas mu gay","lu yg gay anj","gay teriak gay","lu gay asw"])}')
	print ('Coded By MR_DARK')
elif '6281327441039' in mr_dark:
	print(f'_simi bot_: {random.choice(["itu owner aku bang jangan di tag >_<","dia owner aku bang, tolong jangan di tag :)","ada perlu apa sama owner saya? >-<"])}')
	print('Coded By MR_DARK')
elif mr_dark == 'dark':
	print(f'_simi bot_: {random.choice(["ganteng","pro","owner saya tuh","owner saya kak","hengker slebew","kenapa panggil owner saya?"])}')
	print('Coded By MR_DARK')
elif mr_dark == 'wira':
	print('_simi bot_: wibu')
	print('Coded By MR_DARK')
elif mr_dark == 'help':
	print('_simi bot_: apaan anying, tinggal make ae g bisa, wuuuu cupuu')
	print('Coded By MR_DARK')
elif mr_dark == 'kiw':
	print('_simi bot_: kiw itu bocil yang suka nonton bokev')
	print('Coded By MR_DARK')
elif mr_dark == 'owner':
	print('_simi bot_: dark-02')
	print('Coded By MR_DARK')
elif mr_dark == 'aldo':
	print(f'_simi bot_: {random.choice(["hengker epep dia tuh","hati2 dia bisa hek bumi","dia hengker cuy hati2","ngeri hengker epep","esempe"])}')
	print('Coded By MR_DARK')
elif mr_dark == 'bayu':
	print(f'_simi bot_: {random.choice(["Hengker bash","polygon","pejuang kentang","...","yt dia https://youtube.com/channel/UCtu-GcxKL8kJBXpR1wfMgWg"])}')
	print('Coded By MR_DARK')
elif mr_dark == 'silent':
	print('_simi bot_: knp ko disuruh diem bg')
	print('Coded By MR_DARK')
elif mr_dark == 'sofwan':
	print('_simi bot_: kang ngebot discord')
	print('Coded By MR_DARK')
elif mr_dark == 'aushine':
	print('_simi bot_: orang random yang suka read pesan')
	print('Coded By MR_DARK')
elif 'ireng' in mr_dark:
	print(f'_simi bot_: {random.choice(["@PickFord dia ireng ygy","Lu ireng","dasar ireng","ireng teriak ireng","ngaca deck","lu yg ireng asw","dasar ireng g tau diri"])}')
	print('Coded By MR_DARK')
elif 'gay' in mr_dark:
	print('_simi bot_: @Uby dia ril gay cuy')
	print('Coded By MR_DARK')
elif '6283123727298' in mr_dark:
	print(f'_simi bot_: {random.choice(["dia orang gay kata dark","ireng","hati2 dia gay kak!","Jangan deket2 sama orang gay!"])}')
	print('Coded By MR_DARK')
elif 'mau' in mr_dark:
	print('_simi bot_: g mau')
	print('Coded By MR_DARK')
elif 'jam b' in mr_dark:
	sekarang = datetime.now()
	print(f'_simi bot_: {sekarang.strftime("%H:%M:%S")}')
	print('Coded By MR_DARK')
elif 'pacaran' in mr_dark:
	print('_simi bot_: astagfirullah haram brother')
	print('Coded By MR_DARK')
elif 'ammar' and 'Ammar' in mr_dark:
	print('_simi bot_: ammar? esempeh')
	print('Coded By MR_DARK')
elif 'tanggal' in mr_dark:
	print(f'_simi bot_: {date.today()}')
	print('Coded By MR_DARK')
elif '62882296' in mr_dark:
	print(f'_simi bot_: {random.choice(["ammar executed","dia wibu kak","dia masih jomblo kata dark","njer dia masih esempeh"])}')
	print('Coded By MR_DARK')
#elif '6281327441039' in mr_dark:
#	print(f'_simi bot_: {random.choice(["itu owner aku bang jangan di tag >_<","dia owner aku bang, tolong jangan di tag :)","ada perlu apa sama owner saya? >-<"])}')
#	print('Coded By MR_DARK')
#elif 'dark g4y' and 'dark gei' and 'dark ge1' and 'dark ga1' and 'dark gey' and 'd4rk gay' in mr_dark:
#	print(f'_simi bot_: {random.choice(["ndas mu gay","lu yg gay anj","gay teriak gay","lu gay asw"])}')
#	print('Coded By MR_DARK')
else:
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

	dark = requests.get('https://simsimi.info/api/', headers=headers, params=params, cookies=cookies).text
	if 'success' in dark:
	     print('_simi bot_: ', dark.split('"message": "')[1].split('"')[0])
	     print('Coded By MR_DARK')
	else:
	     print('bad respon ')
