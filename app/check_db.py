import pandas as pd
from sqlalchemy import create_engine

# Настройки подключения к PostgreSQL
USER = "ali"
PASSWORD = "ali123"
HOST = "localhost"
PORT = 5432
DB_NAME = "weather_db"
TABLE_NAME = "weather_data"

# Создаём подключение
engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")

# Загружаем таблицу в DataFrame
df = pd.read_sql(f"SELECT * FROM {TABLE_NAME} LIMIT 10;", engine)

print("✅ First 10 rows from weather_data:")
print(df)
