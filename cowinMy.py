from urllib import response
import requests #can be installed using:  pip install requests

PINCODE = "0"

while len(PINCODE) != 6 :
    PINCODE = input("Enter the pincode for which you want the status => ")
    if len(PINCODE) > 6:
        print(f"{PINCODE} is longer than the actual length")
    elif len(PINCODE) < 6:
        print( f"{PINCODE} is shorter than the actual length")

REQ_DATE = input ("Enter the Date to get status (Date format: DD-MM-YYYY) => ")

request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={REQ_DATE}"

response = requests.get(request_link)
raw_JSON  = response.json()



if len(raw_JSON['centers']) != 0 :
    print(f"Total centers in your area is {len(raw_JSON['centers'])}")
else:
    print(f"Unfortunately !! Seems like no center in this area / Kindly re-check the Pincode")

print()

for i in range(len(raw_JSON['centers'])):
    print(f"[{i+1}] Center Name:",raw_JSON['centers'][i]['name'])
    print ("   Date      Vaccine Type    Minimum Age    Available ")
    print ("  ------     -------------   ------------   ----------")

    this_session = raw_JSON['centers'][i]['sessions']

    for j in range(len(this_session)):
        print(f"{this_session[j]['date']}      {this_session[j]['vaccine']}          {this_session[j]['min_age_limit']}             {this_session[j]['available_capacity']}")