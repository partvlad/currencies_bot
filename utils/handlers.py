"""Обработчик параметров"""
import os
from http import HTTPStatus

import  requests

from configs import log_configured
from configs.base import API_URL
# from exceptions import APIException, ServiceException
from requests import Response
from telegram.ext import ContextTypes

logger = log_configured.getLogger(__name__)


def get_token(key: str) -> str:
    """Проверяем наличие токена"""
    token: str | None = os.getenv(key)
    if token is not None:
        return token
    raise APIException('Не передан токен для доступа к боту')