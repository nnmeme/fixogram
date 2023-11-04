from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..state import State


@dataclass(frozen=True)
class UserKey:
    chat_id: int
    user_id: int


class BaseStorage(ABC):
    @abstractmethod
    async def set_state(self, key: UserKey, state: State) -> None:
        ...

    @abstractmethod
    async def get_state(self, key: UserKey) -> State:
        ...

    @abstractmethod
    async def get_data(self, key: UserKey) -> dict:
        ...

    @abstractmethod
    async def set_data(self, key: UserKey, data: dict) -> dict:
        ...