from fastapi import FastAPI

app = FastAPI()

# poetry run fastapi dev fastapi_zero/app.py
# poetry shell
# ruff check .
# ruff check --fix


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
