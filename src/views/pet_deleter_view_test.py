#pylint: disable=C0301
from unittest.mock import Mock
from src.views.pet_deleter_view import PetDeleterView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface

def test_pet_deleter_view():
    # Criando um mock do controlador
    mock_controller = Mock(spec=PetDeleterControllerInterface)
    
    view = PetDeleterView(mock_controller)
    
    http_request = HttpRequest(param={"name": "Buddy"})

    response = view.handle(http_request)
    
    mock_controller.delete.assert_called_once_with("Buddy") # Verificando se o método delete foi chamado corretamente
    
    # Verificando se o retorno é o esperado
    expected_response = HttpResponse(status_code=200)
    assert response.status_code == expected_response.status_code
