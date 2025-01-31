from unittest.mock import Mock
from src.views.person_finder_view import PersonFinderView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

def test_handle_person_found():
    # Criando um mock do controller
    mock_controller = Mock()
    mock_controller.find.return_value = {"id": 1, "name": "Guilherme"}

    # Criando a view com o mock
    view = PersonFinderView(mock_controller)

    # Simulando um HttpRequest com um parâmetro de ID
    http_request = HttpRequest(param={"id": 1})

    # Chamando o método handle
    response = view.handle(http_request)

    # Criando a resposta esperada
    expected_response = HttpResponse(status_code=200, body={"id": 1, "name": "Guilherme"})

    # Testando se a resposta está correta
    assert response.status_code == expected_response.status_code
    assert response.body == expected_response.body
