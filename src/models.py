# modelo: representação do banco de dados
# view: como os dados vão vir - do request / schema
# não necessariamente o schema tem que ser igual ao model
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now())