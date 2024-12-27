
import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_api_key"

# Custom your latitude and longitude here
lat = 14.020100
lon = 100.523567

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

res = requests.get(endpoint, params=params)
will_rain = False

if res.status_code == requests.codes.ok:
    data = res.json()
    data = data["list"][0:4]
    data = [int(ele["weather"][0]["id"]) for ele in data]
    if data[3] > 800:
        will_rain = True

if will_rain:
    account_sid = "your_id"
    auth_token = "your_token"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="There will rain in the next 12 hours in your area. Don't forget to bring an umbrella",
        from_="from_number",
        to="to_number",
    )

    print(message.body)
