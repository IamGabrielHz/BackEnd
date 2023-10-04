from sqlmodel import create_engine, SQLModel


def get_engine():
    #url = 'sqlite:///database.db'
    url = 'postgresql+psycopg2://tasks_api_user:B0cvydl1RsTc8107sMeIVoz9niqgJIj0@dpg-ckerlgvs0fgc73c55hgg-a.oregon-postgres.render.com/tasks_api'
    return create_engine(url, echo=True)


def create_tables():
    SQLModel.metadata.create_all(get_engine())
