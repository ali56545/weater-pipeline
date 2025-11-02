def load_weather_data(df, file_path="weather_data.csv"):
    df.to_csv(file_path, index=False)
    print(f"✅ Data saved to {file_path}")
