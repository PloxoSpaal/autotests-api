from httpx import Client
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],  # Логируем исходящие HTTP-запросы
            "response": [log_response_event_hook]  # Логируем полученные HTTP-ответы
        }
    )