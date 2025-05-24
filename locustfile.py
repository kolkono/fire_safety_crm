from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Время ожидания между запросами

    @task
    def create_client(self):
        self.client.post("/clients/create/", {
            "name": "Тест Клиент",
            "phone": "123456789",
            "email": "test@example.com",
            "address": "Улица Тестовая",
            "city": "Москва"
        })