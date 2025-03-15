# o schema do pydantic

from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True #pra falar com a orm