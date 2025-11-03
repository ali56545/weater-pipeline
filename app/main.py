from extract.extract_data import extract_weather_data
from transform.transform_data import transform_weather_data
from load.load_data import load_weather_data
from app.config_loader import load_config
from load_to_db import load_to_postgres_df  # новая функция для DataFrame напрямую

def main():
    print("🚀 Starting ETL pipeline...")

    # 0. Создаём папку для CSV на случай, если захотим сохранить
    import os
    os.makedirs("data", exist_ok=True)

    # Load config
    config = load_config()
    cities = config["cities"]

    # 1. Extract
    df = extract_weather_data(cities)
    print("✅ Data extracted for all cities!")

    # 2. Transform
    df = transform_weather_data(df)
    print("✅ Data transformed!")

    # 3. Load (CSV) — опционально
    load_weather_data(df)
    print("✅ Data saved to CSV!")

    # 4. Load directly to PostgreSQL
    load_to_postgres_df(
        df=df,
        user="ali",
        password="ali123",
        host="localhost",
        port=5432,
        db_name="weather_db",
        table_name="weather_data"
    )
    print("🎉 Data loaded into PostgreSQL successfully!")

if __name__ == "__main__":
    main()
