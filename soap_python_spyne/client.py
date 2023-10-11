from zeep import Client

# Создаем клиент, указывая адрес WSDL-файла
client = Client("http://localhost:8000/?wsdl")

# Вызываем метод say_hello сервиса, передавая ему параметр "World"
result = client.service.say_hello("World")

# Выводим результат на экран
print(result)  # Hello, World!
