from typing import Callable, Generic, Type, TypeVar

from taipan_di.interfaces import BaseDependencyProvider

__all__ = ["SingletonScope"]

T = TypeVar("T")


class SingletonScope(Generic[T]):
    def __init__(self, creator: Callable[[BaseDependencyProvider], T]) -> None:
        self._creator = creator
        self._memoized_instance = None

    def get_instance(self, container: BaseDependencyProvider) -> T:
        if self._memoized_instance is None:
            self._memoized_instance = self._creator(container)

        return self._memoized_instance
