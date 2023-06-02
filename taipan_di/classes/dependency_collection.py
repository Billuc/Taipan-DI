from typing import Callable, Type, TypeVar

from taipan_di.interfaces import BaseDependencyProvider

from .dependency_container import DependencyContainer
from .instanciate_service import instanciate_service
from .scopes import FactoryScope, SingletonScope


T = TypeVar("T")
U = TypeVar("U")


class DependencyCollection:
    def __init__(self) -> None:
        self._container = DependencyContainer()

    # Public methods

    def register_singleton_creator(
        self, type: Type[T], creator: Callable[[BaseDependencyProvider], T]
    ) -> None:
        service = SingletonScope(creator)
        self._container.register(type, service)

    def register_singleton_instance(self, type: Type[T], instance: T) -> None:
        creator = lambda provider: instance
        self.register_singleton_creator(type, creator)

    def register_singleton(
        self, interface_type: Type[T], implementation_type: Type[U] = None
    ) -> None:
        if implementation_type is None:
            implementation_type = interface_type
            
        creator = lambda provider: instanciate_service(implementation_type, provider)
        self.register_singleton_creator(interface_type, creator)

    def register_factory_creator(
        self, type: Type[T], creator: Callable[[BaseDependencyProvider], T]
    ) -> None:
        service = FactoryScope(creator)
        self._container.register(type, service)

    def register_factory(
        self, interface_type: Type[T], implementation_type: Type[U] = None
    ) -> None:
        if implementation_type is None:
            implementation_type = interface_type

        creator = lambda provider: instanciate_service(implementation_type, provider)
        self.register_factory_creator(interface_type, creator)

    def build(self) -> BaseDependencyProvider:
        return self._container.build()
