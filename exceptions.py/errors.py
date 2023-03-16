"""Кастомнные классы обработки ошибок"""


class APIException(Exception):
    """Ошибка в работе API."""

    ...


class ServiceException(Exception):
    """Ошибка в работе сервиса курса валют."""

    ...
