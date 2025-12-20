"""
Rain Alert Notifier
Fetches a 12-hour weather forecast using the OpenWeatherMap API.
If rain is detected (based on Weather Condition IDs), it sends an SMS
notification to the user via the Twilio API.
"""

import requests
from twilio.rest import Client

# --- Configuration & API Setup ---
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "your_api_key"

# Twilio Credentials
ACCOUNT_SID = "your_id"
AUTH_TOKEN = "your_token"

# Custom coordinates (Latitude/Longitude)
LAT = 14.020100
LON = 100.523567

params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,  # Optional: Limit results to the next 4 timestamps (12 hours)
}

# --- Data Fetching ---
res = requests.get(ENDPOINT, params=params)
will_rain = False

if res.status_code == requests.codes.ok:
    data = res.json()

    # The API returns forecasts in 3-hour increments.
    # data["list"][0:4] captures the next 12 hours of weather.
    forecast_list = data["list"][0:4]

    # Weather Condition Codes (e.g., 2xx = Thunderstorm, 5xx = Rain)
    # Using list comprehension to extract the 'id' for each 3-hour block
    weather_ids = [int(hour_data["weather"][0]["id"]) for hour_data in forecast_list]

    # Logic: If any ID is between 200 and 600, it indicates rain or storm
    for code in weather_ids:
        if code < 700:  # 200-600 codes specifically represent rain/snow/storms
            will_rain = True
            break

# --- SMS Notification ---
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="It's going to rain in the next 12 hours. ☔ Don't forget an umbrella!",
        from_="from_number",
        to="to_number",
    )

    print(f"Notification Sent: {message.status}")
