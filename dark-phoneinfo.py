import phonenumbers, shlex, sys
from phonenumbers import carrier, geocoder, timezone
mr_darkk = " ".join(map(shlex.quote, sys.argv[1:]))
mr_dark = f"+{mr_darkk}"
#mobileNo=input("Mobile no. with country code:")
print (f"Info Nomor: {mr_dark}")
mobileNo=mr_dark
mobileNo=phonenumbers.parse(mobileNo)
print(timezone.time_zones_for_number(mobileNo))
print('```provider / sim```: '+carrier.name_for_number(mobileNo,"en"))
print('```Negara```: '+geocoder.description_for_number(mobileNo,"en"))
print("```Nomor Yang Valid?```:",phonenumbers.is_valid_number(mobileNo))
print("```possibility```:",phonenumbers.is_possible_number(mobileNo))
print ("_Script By MR_DARK_")
