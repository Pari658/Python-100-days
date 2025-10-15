import requests
import datetime
import smtplib

MY_LAT = 22.691586
MY_LONG = 72.863365

def isIssNear():
  responseISS = requests.get("http://api.open-notify.org/iss-now.json")
  responseISS.raise_for_status()
  longitude = float(responseISS.json()["iss_position"]["longitude"])
  latitude = float(responseISS.json()["iss_position"]["latitude"])
  if(MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <=MY_LONG):
    return True

def isNight():
  parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
  }
  response = requests.get("https://api.sunrise-sunset.org/json" ,params = parameters)
  response.raise_for_status()
  sunRise = response.json()["results"]["sunrise"]
  sunSet = response.json()["results"]["sunset"]
  data = (sunRise,sunSet)
  sunRiseHour = int(sunRise.split("T")[1].split(":")[0])
  sunSetHour = int(sunSet.split("T")[1].split(":")[0])
  timeNowHour = datetime.datetime.now().hour
  if(timeNowHour >= sunSetHour or timeNowHour <= sunRiseHour):
    return True

def sendmail():
  with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login("parijpatel07@gmail.com","idbw dvsq herb vdyh")
    connection.sendmail(from_addr = "parijpatel07@gmail.com",to_addrs="24cp035@bvmengineering.ac.in",msg = f"subject: LookUp there is an iss")
    
if isIssNear() and isNight():
  sendmail()
