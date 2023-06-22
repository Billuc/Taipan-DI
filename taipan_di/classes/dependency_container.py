from typing import Any, Dict, Type, cast, TypeVar

from taipan_di.interfaces import BaseDependencyProvider, BaseScope

from .dependency_provider import DependencyProvider

__all__ = ["DependencyContainer"]

T = TypeVar("T")


class DependencyContainer:
    def __init__(self) -> None:
        self._services = cast(Dict[Type[Any], BaseScope], {})

    def contains(self, type: Type[Any]) -> bool:
        return type in self._services

    def register(self, type: Type[T], service: BaseScope[T]) -> None:
        self._services[type] = service

    def build(self) -> BaseDependencyProvider:
        provider = DependencyProvider(self._services)
        return provider
