import os,sys
bruh = sys.argv[1];
os.system(f"curl http://uzingela.co.za/{bruh} -o {bruh}")
print (f"*Transfer file from desktop success!, saved file name*: {bruh}")