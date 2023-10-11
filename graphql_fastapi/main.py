import strawberry
from typing import Dict, Optional
from fastapi import FastAPI
from strawberry.asgi import GraphQL


# Определяем тип User с полями name и age
@strawberry.type
class User:
    name: str
    age: int


# Класс Database использует словарь для хранения пользователей
# ВНИМАНИЕ: Это не самый лучший способ хранения данных, не используйте его в продакшене
class Database:
    def __init__(self):
        self.users: Dict[str, User] = {}

    # Метод add_user добавляет пользователя в словарь
    def add_user(self, user: User):
        self.users[user.name] = user

    # Метод get_user возвращает пользователя по имени или None, если такого пользователя нет
    def get_user(self, name: str) -> Optional[User]:
        return self.users.get(name)


# Создаем экземпляр класса Database
db = Database()


# Определяем тип Query с полем user, которое возвращает пользователя по имени
@strawberry.type
class Query:
    @strawberry.field
    def user(self, name: str) -> Optional[User]:
        return db.get_user(name)


# Определяем тип Mutation с полем create_user, которое создает нового пользователя
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, age: int) -> User:
        user = User(name=name, age=age)
        db.add_user(user)
        return user


# Создаем схему GraphQL с типами Query и Mutation
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Создаем приложение FastAPI и добавляем маршруты для GraphQL
graphql_app = GraphQL(schema)
app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

# Запускаем приложение с помощью сервера uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


# Перейдите на http://127.0.0.1:8000/graphql для открытия интерфейса GraphQL
#
# Примеры запросов:
# Создать пользователя
# mutation {
#   createUser(name: "egor", age: 23) {
#     name
#     age
#   }
# }
#
# Получить пользователя
# query {
#   user(name: "egor") {
#     name
#     age
#   }
# }
