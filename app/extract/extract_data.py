import requests
import pandas as pd

def extract_weather_data(cities):
    url = "https://api.open-meteo.com/v1/forecast"
    all_data = []

    for city in cities:
        params = {
            "latitude": city["lat"],
            "longitude": city["lon"],
            "hourly": "temperature_2m",
            "forecast_days": 1
        }

        response = requests.get(url, params=params)
        data = response.json()

        df = pd.DataFrame({
            "time": data["hourly"]["time"],
            "temperature": data["hourly"]["temperature_2m"]
        })
        df["city"] = city["name"]
        all_data.append(df)

    full_df = pd.concat(all_data, ignore_index=True)
    return full_df
