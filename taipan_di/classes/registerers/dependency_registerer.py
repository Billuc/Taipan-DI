from typing import Type, TypeVar, Generic

from taipan_di.interfaces import BaseDependencyContainer

from .singleton_registerer import SingletonRegisterer
from .factory_registerer import FactoryRegisterer

__all__ = ["DependencyRegisterer"]


T = TypeVar("T")


class DependencyRegisterer(Generic[T]):
    def __init__(
        self, type_to_register: Type[T], container: BaseDependencyContainer
    ) -> None:
        self._type_to_register = type_to_register
        self._container = container

    def as_singleton(self) -> SingletonRegisterer[T]:
        registerer = SingletonRegisterer[T](self._type_to_register, self._container)
        return registerer

    def as_factory(self) -> FactoryRegisterer[T]:
        registerer = FactoryRegisterer[T](self._type_to_register, self._container)
        return registerer
