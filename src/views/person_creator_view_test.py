from src.views.person_creator_view import PersonCreatorView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class MockPersonCreatorController:
    def create(self, person_info):
        return {"id": 1, "name": person_info["name"], "age": person_info["age"]}

def test_handle_should_return_201_with_person_info():
    mock_controller = MockPersonCreatorController()
    view = PersonCreatorView(mock_controller)
    request_data = {"name": "John Doe", "age": 30}
    http_request = HttpRequest(body=request_data)

    response = view.handle(http_request)

    expected_response = HttpResponse(status_code=201, body={"id": 1, "name": "John Doe", "age": 30})
    assert response.status_code == expected_response.status_code
    assert response.body == expected_response.body
