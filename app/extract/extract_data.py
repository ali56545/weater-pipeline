import requests
import pandas as pd

def extract_weather_data():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 42.87,  # Бишкек
        "longitude": 74.59,
        "hourly": "temperature_2m",
        "forecast_days": 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"]
    })
    return df
