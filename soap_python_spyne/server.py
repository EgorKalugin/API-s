from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


# Создаем сервис, который будет приветствовать пользователей
class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hello, {name}!"


# Создаем приложение, которое будет использовать наш сервис
application = Application(
    [HelloWorldService],  # Передаем список сервисов, которые будут использоваться
    tns="example.com",  # Указываем namespace
    in_protocol=Soap11(validator="lxml"),  # Указываем протокол входящих сообщений
    out_protocol=Soap11(),  # Указываем протокол исходящих сообщений
)

# Если запускаем файл напрямую, то запускаем сервер
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server("localhost", 8000, wsgi_app)  # Создаем сервер
    server.serve_forever()  # Запускаем сервер и ожидаем запросов



