def transform_weather_data(df):
    df["temperature_celsius"] = df["temperature"]
    df["temperature_fahrenheit"] = df["temperature"] * 9/5 + 32
    return df
