from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Buddy", type="Dog", id=47)
        ]
    
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 1,
            "attributes": [
                {"name": "Buddy", "id": 47}

            ]
        }
    }
     
    assert response == expected_response
