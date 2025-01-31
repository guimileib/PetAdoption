from src.controllers.pet_deleter_controller import PetDeleterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PetListerView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller 
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.params['name']
        self.__controller.delete(name)

        return HttpResponse(status_code=200)
