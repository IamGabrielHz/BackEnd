from sqlmodel import create_engine


def obter_engine():
  db_url = 'sqlite:///database.db'
  engine = create_engine(db_url, echo=True)
  
  return engine