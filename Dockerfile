FROM python:3.9-slim as base
LABEL image_name="python-kotik"
LABEL maintainer="Kotik Zasranets <kotik@.ru>"

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Установка poetry
RUN pip install poetry && poetry self add 'poethepoet[poetry_plugin]'
# Отключает питоновский кеш.
ENV PYTHONDONTWRITEBYTECODE 1
# Позволяет корректно выводить логи python.
ENV PYTHONUNBUFFERED 1

# Установка питонячьих библиотек
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Копирование остальных файлов проекта
COPY . /app

# Запуск pytest
CMD ["poetry", "run", "pytest"]
