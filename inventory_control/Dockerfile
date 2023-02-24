# Використовуємо офіційний Python runtime як базовий імедж
FROM python:3.10-slim

# Встановлюємо системні залежності
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        postgresql-client \
        && \
    rm -rf /var/lib/apt/lists/*

# Створюємо робочу директорію та копіюємо файли проекту
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Встановлюємо залежності Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
    #pip install pipenv && \
    #pipenv install django

# Запускаємо сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
