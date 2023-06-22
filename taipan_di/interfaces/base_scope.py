import abc
from typing import Type, TypeVar, Protocol

from .base_dependency_provider import BaseDependencyProvider

__all__ = ["BaseScope"]

T = TypeVar("T", covariant=True)


class BaseScope(Protocol[T]):
    @abc.abstractmethod
    def get_instance(self, container: BaseDependencyProvider) -> T:
        raise NotImplementedError()
