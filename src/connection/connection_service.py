from abc import ABCMeta, abstractmethod
from tornado.websocket import WebSocketHandler
from pydantic import BaseModel

from .models import (
    PlayerData,
    ConnectionCode,
    ConnectionToGameResult,
)


class ConnectionService(metaclass=ABCMeta):
    @abstractmethod
    def connect(self, socket: WebSocketHandler, player_data: PlayerData) -> BaseModel: ...

    @abstractmethod
    def remove_socket_if_exists(self, socket: WebSocketHandler) -> ConnectionToGameResult: ...
