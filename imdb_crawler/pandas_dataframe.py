import os

import pandas as pd


def query_db_and_create_dataframe():
    db_host = os.getenv("DB_HOST", "localhost")
    db_name = os.getenv("DB_NAME", "seu_banco")
    db_user = os.getenv("DB_USER", "seu_usuario")
    db_password = os.getenv("DB_PASSWORD", "sua_senha")
    db_port = os.getenv("DB_PORT", "sua_porta")

    db_uri = (
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

    df = pd.read_sql_query("SELECT * FROM movies ORDER BY rank", db_uri)

    return df
