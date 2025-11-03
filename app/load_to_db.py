from sqlalchemy import create_engine

def load_to_postgres_df(df, user, password, host, port, db_name, table_name):
    """
    Загружает DataFrame напрямую в PostgreSQL
    """
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Data loaded successfully into table '{table_name}'!")
