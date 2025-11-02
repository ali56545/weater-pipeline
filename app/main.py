from extract.extract_data import extract_weather_data
from transform.transform_data import transform_weather_data
from load.load_data import load_weather_data

def main():
    print("🚀 Starting ETL pipeline...")

    # 1. Extract
    df = extract_weather_data()
    print("✅ Data extracted!")

    # 2. Transform
    df = transform_weather_data(df)
    print("✅ Data transformed!")

    # 3. Load
    load_weather_data(df)
    print("🎉 Pipeline finished successfully!")

if __name__ == "__main__":
    main()
