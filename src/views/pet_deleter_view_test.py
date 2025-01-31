from unittest.mock import Mock
from src.views.pet_deleter_view import PetDeleterView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.pet_deleter_controller import PetDeleterControllerInterface

def test_pet_deleter_view():
    # Criando um mock do controlador
    mock_controller = Mock(spec=PetDeleterControllerInterface)
    
    # Criando a instância da view com o controlador mockado
    view = PetDeleterView(mock_controller)
    
    # Criando um HttpRequest de teste
    http_request = HttpRequest(param={"name": "Buddy"})
    
    # Chamando o método handle
    response = view.handle(http_request)
    
    # Verificando se o método delete foi chamado corretamente
    mock_controller.delete.assert_called_once_with("Buddy")
    
    # Verificando se o retorno é o esperado
    expected_response = HttpResponse(status_code=200)
    assert response.status_code == expected_response.status_code
