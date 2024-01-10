from core.router import HTTPRouter
from controllers.MainController import main_controller

def use_routes(router: HTTPRouter):
    router.get('/', main_controller.index)
    router.get('/message', main_controller.message)
    router.post('/message', main_controller.message_handler)