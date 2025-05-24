# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Указываем переменную окружения для Django
ENV PYTHONUNBUFFERED=1

# Команда запуска development-сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
