FROM python:3.12

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock* /code/

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

COPY . /code/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]