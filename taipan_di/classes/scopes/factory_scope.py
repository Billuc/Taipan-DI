from typing import Callable, Generic, TypeVar

from taipan_di.interfaces import BaseDependencyProvider

__all__ = ["FactoryScope"]

T = TypeVar("T")


class FactoryScope(Generic[T]):
    def __init__(self, creator: Callable[[BaseDependencyProvider], T]) -> None:
        self._creator = creator

    def get_instance(self, container: BaseDependencyProvider) -> T:
        instance = self._creator(container)
        return instance
