# Mostrando para meu código que a tabela Pets existe
from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets" # o nome da tabela

    # Colunas:
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"Pet [name={self.name}, type={self.type}]"  # Retorna o nome e o tipo do pet
