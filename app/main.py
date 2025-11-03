from extract.extract_data import extract_weather_data
from transform.transform_data import transform_weather_data
from load.load_data import load_weather_data
from app.config_loader import load_config

def main():
    print("🚀 Starting ETL pipeline...")

    # Load config
    config = load_config()
    cities = config["cities"]

    # 1. Extract
    df = extract_weather_data(cities)
    print("✅ Data extracted for all cities!")

    # 2. Transform
    df = transform_weather_data(df)
    print("✅ Data transformed!")

    # 3. Load
    load_weather_data(df)
    print("🎉 Pipeline finished successfully!")

if __name__ == "__main__":
    main()
