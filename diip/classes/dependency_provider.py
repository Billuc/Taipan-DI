from typing import Dict, Type, TypeVar

from diip.errors import DIIPUnregisteredError
from diip.interfaces import BaseDependencyProvider, BaseScope

T = TypeVar("T")


class DependencyProvider(BaseDependencyProvider):
    def __init__(self, services: Dict[Type, BaseScope]) -> None:
        self._services = services.copy()

    def contains(self, type: Type[T]) -> bool:
        return type in self._services

    def resolve(self, type: Type[T]) -> T:
        if not type in self._services:
            raise DIIPUnregisteredError("Service %s is not registered", str(type))

        service = self._services[type]
        result = service.get_instance(type, self)

        return result
