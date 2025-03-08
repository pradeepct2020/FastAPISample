from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DBURL = "sqlite:///C:\\Pradeep\\Interview-Questions\\Python-Excersice\\Libaray-Management\\library.db"
# DBURL = "sqlite:////c/Pradeep/Interview-Questions/Python-Excersice/Libaray-Management/library.db"
engine = create_engine(DBURL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
 
    finally:
        db.close()
 
