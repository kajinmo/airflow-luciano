# poderia estar no models, mas pra não precisar mexer nele se mudar de banco de dados
# estou colocando no db

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

#SQLALCHEMY_DATABASE_URL = "sqlite:///./pokemon.db"

engine = create_engine("URLPOSTGRES")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

