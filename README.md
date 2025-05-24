🧾 О проекте
Этот репозиторий представляет собой учебный проект, включающий в себя:

Разработку веб-приложения для управления клиентами на Django с административной панелью,

Визуализацию данных клиентов по городам с помощью Plotly,

Реализацию REST API для работы с клиентами через Django REST Framework,

Контейнеризацию проекта с использованием Docker,

Автоматическое функциональное тестирование с Playwright,

Проведение нагрузочного тестирования с помощью Locust.


🛠 Структура проекта
fire_safety_crm/
│
├── clients/                      # Django приложение "clients"
│   ├── migrations/               # Миграции базы данных
│   ├── templates/clients/        # HTML шаблоны для приложения clients
│   │   ├── client_form.html
│   │   ├── client_list.html
│   │   ├── client_report.html
│   ├── __init__.py
│   ├── admin.py
│   ├── api_urls.py               # URLы для API приложения clients
│   ├── apps.py
│   ├── forms.py                 # Формы Django (ClientForm)
│   ├── models.py                # Модели данных (Client и т.д.)
│   ├── serializers.py           # DRF сериализаторы (ClientSerializer)
│   ├── tests.py                 # Тесты (питоновые)
│   ├── urls.py                  # URLы для фронтенд приложения clients
│   ├── views.py                 # Вьюхи (функциональные и классовые)
│
├── fire_safety_crm/              # Главная папка проекта (settings и пр.)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py                  # Главные URLы проекта, включает clients.urls и clients.api_urls
│   ├── wsgi.py
│
├── tests/                       # Playwright тесты (js/ts) и возможно другие
│   ├── client_list.spec.ts
│
├── Dockerfile                   # Докерфайл для контейнеризации
├── docker-compose.yml           # Compose файл (если есть)
├── manage.py                   # Скрипт запуска Django
├── requirements.txt            # Список зависимостей Python
├── package.json                # Для npm/Playwright и автотестов
├── README.md
└── .gitignore
