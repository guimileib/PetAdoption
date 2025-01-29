import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='interação com banco de dados')
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets() #  Lista de pets
    print()
    print(response) # Vai printar a lista de pets

def test_delete_pets():
    name = 'belinha'

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name) # Deleta o pet
