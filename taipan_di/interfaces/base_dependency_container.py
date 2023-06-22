import abc
from typing import Any, Type, Protocol, TypeVar

from .base_dependency_provider import BaseDependencyProvider
from .base_scope import BaseScope

__all__ = ["BaseDependencyContainer"]

T = TypeVar("T")


class BaseDependencyContainer(Protocol):
    @abc.abstractmethod
    def contains(self, type: Type[Any]) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def register(self, type: Type[T], service: BaseScope[T]) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def build(self) -> BaseDependencyProvider:
        raise NotImplementedError
