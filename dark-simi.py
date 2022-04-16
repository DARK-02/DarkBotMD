import os,sys,requests,shlex
from requests import get
mr_dark = " ".join(map(shlex.quote, sys.argv[1:]))
mr_dark_url = f'http://api.simsimi.net/v2/?text={mr_dark}&lc=id'
dark = requests.get(mr_dark_url)
if dark.status_code == 200:
     print('')
     print('_simi bot_: ', dark.json().get('success'))
     print('```Copyright By Mr_Dark 2022 🫠```')
else:
     print('bad respon ')
