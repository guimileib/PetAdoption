from unittest.mock import Mock
from src.views.pet_lister_view import PetListerView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.pet_lister_controller import PetListerControllerInterface

def test_pet_lister_view():
    # Criando um mock do controlador
    mock_controller = Mock(spec=PetListerControllerInterface)
    
    # Configurando o retorno esperado do método list() do controlador
    mock_controller.list.return_value = [
        {"name": "Fluffy", "id": 4},
        {"name": "Buddy", "id": 47}
    ]
    
    # Criando a instância da view com o controlador mockado
    view = PetListerView(mock_controller)
    
    # Criando um HttpRequest de teste (no caso, sem corpo necessário para esse caso)
    http_request = HttpRequest(body=None, param={})
    
    # Chamando o método handle
    response = view.handle(http_request)
    
    # Verificando se o método list foi chamado corretamente
    mock_controller.list.assert_called_once()
    
    # Verificando se a resposta tem status_code correto e o corpo correto
    expected_response = HttpResponse(status_code=200, body=[
        {"name": "Fluffy", "id": 4},
        {"name": "Buddy", "id": 47}
    ])
    assert response.status_code == expected_response.status_code
    assert response.body == expected_response.body
