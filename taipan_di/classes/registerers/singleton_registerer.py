from typing import Callable, Type, Generic, TypeVar

from taipan_di.classes.scopes import SingletonScope
from taipan_di.classes.tools import instanciate_service

from taipan_di.interfaces import BaseDependencyProvider, BaseDependencyContainer

__all__ = ["SingletonRegisterer"]

T = TypeVar("T")


class SingletonRegisterer(Generic[T]):
    def __init__(
        self, type_to_register: Type[T], container: BaseDependencyContainer
    ) -> None:
        self._type_to_register = type_to_register
        self._container = container

    def with_implementation(self, implementation_type: Type[T]) -> None:
        creator = lambda provider: instanciate_service.instanciate_service(
            implementation_type, provider
        )
        self._register(creator)

    def with_creator(self, creator: Callable[[BaseDependencyProvider], T]) -> None:
        self._register(creator)

    def with_instance(self, instance: T) -> None:
        creator = lambda provider: instance
        self._register(creator)

    def with_self(self) -> None:
        creator = lambda provider: instanciate_service.instanciate_service(
            self._type_to_register, provider
        )
        self._register(creator)

    def _register(self, creator: Callable[[BaseDependencyProvider], T]) -> None:
        scope = SingletonScope[T](creator)
        self._container.register(self._type_to_register, scope)
