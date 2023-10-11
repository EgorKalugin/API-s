from http.server import BaseHTTPRequestHandler, HTTPServer
import json


# Создаем класс-обработчик запросов
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Обработчик GET-запросов
    def do_GET(self):
        # Если путь запроса равен '/', то возвращаем 'Hello, World!' в виде HTML-страницы
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
            return
        # Если путь запроса равен '/api', то возвращаем 'Hello, World!' в виде JSON-объекта
        elif self.path == "/api":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": "Hello, World!"}
            self.wfile.write(json.dumps(response).encode())
            return
        # Если путь запроса неизвестен, то возвращаем ошибку 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return

    # Обработчик POST-запросов
    def do_POST(self):
        # Если путь запроса равен '/api', то возвращаем 'Hello, World!' в виде JSON-объекта
        if self.path == "/api":
            # Получаем заголовки запроса
            content_length = int(self.headers.get("Content-Length", 0))
            content_type = self.headers.get("Content-Type")

            # Если тело запроса не пустое, то получаем его
            if content_length > 0:
                body = self.rfile.read(content_length).decode("utf-8")
            else:
                body = None

            # Выводим тело запроса, content_length и content_type в консоль
            print(f"Тело запроса: {body}")
            print(f"content_length: {content_length}")
            print(f"content_type: {content_type}")

            # Отправляем ответ в формате JSON
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # Если тело запроса не пустое, то возвращаем его в ответе
            if body:
                response = {"message": f"Получил: {body}"}
            else:
                response = {"message": "Получил пустой запрос"}
            self.wfile.write(json.dumps(response).encode())
            return
        # Если путь запроса неизвестен, то возвращаем ошибку 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return


# Функция запуска сервера
def run_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Starting server...")
    httpd.serve_forever()


# Если файл запускается напрямую, то запускаем сервер
if __name__ == "__main__":
    run_server()
