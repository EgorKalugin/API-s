Простой пример gRPC сервиса на Python:

1. Определение протокола:

```protobuf
syntax = "proto3";

service GreetingService {
  rpc SayHello (HelloRequest) returns (HelloResponse) {}
}

message HelloRequest {
  string name = 1;
}

message HelloResponse {
  string message = 1;
}
```

2. Генерация Python-кода из .proto файла:

Установите gRPC-инструментарий для Python, если еще не установлен, используя команду `pip install grpcio`.

Затем сгенерируйте Python-код из .proto файла с помощью команды:
```
python -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ ./greeting.proto
```
Должны появится два файла: `greeting_pb2.py` и `greeting_pb2_grpc.py`.

3. Реализация сервера в server.py
4. Реализация клиента в client.py

В этом примере мы создаем простой gRPC сервис для приветствия пользователей. Клиент отправляет запрос с именем, сервер получает это имя и возвращает приветствие вместе с сообщением.

Установите необходимые зависимости из req.txt(pip install -r ./req.txt) и запустите сервер (`python server.py`). Затем запустите клиент (`python client.py`) и введите свое имя. Вы должны увидеть ответ от сервера с приветствием.
