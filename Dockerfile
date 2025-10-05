# Базовый образ Python
FROM python:3.12.8-slim

# Установка рабочей директории
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение
COPY . .

# Команда запуска приложения (тесты с allure)
CMD ["pytest", "--alluredir=allure-results"]
