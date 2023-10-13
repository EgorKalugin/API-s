from typing import List
from fastapi import FastAPI

import requests


def get_cat_facts() -> List[str]:
    URL = "https://cat-fact.herokuapp.com/facts"  # URL для получения фактов о котах
    response = requests.get(URL)  # отправляем GET-запрос на URL
    facts_json = response.json()  # получаем ответ в формате JSON
    list_of_facts = []
    for fact in facts_json:
        if fact.get("text"):  # если в факте есть текст
            list_of_facts.append(fact["text"])  # добавляем текст факта в список
        else: # в противном случае
            print(f"В факте {fact} нет текста")  # выводим сообщение об ошибке
    return list_of_facts


app = FastAPI()


@app.get("/cat_fact")
def get_cat_facts_handler() -> List[str]:
    cat_facts = get_cat_facts()  # получаем список фактов о котах
    return cat_facts


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)  # запускаем сервер с помощью Uvicorn