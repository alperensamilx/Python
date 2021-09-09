import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "17327553eca4b7ce1c77e8058f078671"
account_sid = 'AC0b9806aea491d718f8c11fc200a31478'
auth_token = 'cb77bec527886d5f9171fa19ef62984f'

weather_params = {
    "lat": 40.653671,
    "lon": 35.833618,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][0:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+12025179832',
        to='+905417478669'
    )
print(message.status)
