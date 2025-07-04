from httpx import Client
from clients.event_hooks import curl_event_hook
from config import settings  # Импортируем настройки


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(
        timeout=settings.http_client.timeout,  # Таймаут теперь берётся из настроек
        base_url=settings.http_client.client_url,  # Базовый URL также из настроек
        event_hooks={"request": [curl_event_hook]}
    )