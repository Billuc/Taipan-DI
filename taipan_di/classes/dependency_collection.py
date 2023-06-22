from typing import Type, TypeVar

from taipan_di.interfaces import BaseDependencyProvider

from .dependency_container import DependencyContainer
from .tools import PipelineLink
from .registerers import DependencyRegisterer, PipelineRegisterer

__all__ = ["DependencyCollection"]

T = TypeVar("T")
U = TypeVar("U")


class DependencyCollection:
    """
    The `DependencyCollection` allows you to register your services.

    It exposes 2 methods to initiate registration processes : `register` and `register_pipeline`.

    To resolve your services, you have to first `build` a `BaseDependencyProvider`.
    """

    def __init__(self) -> None:
        self._container = DependencyContainer()

    ## Standard register

    def register(self, type_to_register: Type[T]) -> DependencyRegisterer[T]:
        """
        Initiate the registration of a service.

        Returns a registerer to register the service as wanted.
        """
        registerer = DependencyRegisterer[T](type_to_register, self._container)
        return registerer

    ## Pipeline

    def register_pipeline(
        self, interface_type: Type[PipelineLink[T, U]]
    ) -> PipelineRegisterer[T, U]:
        """
        Initiate the registration of a service as a pipeline.

        Returns a registerer to be used to add the links and then register the service.
        """
        registrator = PipelineRegisterer[T, U](interface_type, self._container)
        return registrator

    ## Build

    def build(self) -> BaseDependencyProvider:
        """
        Builds the service provider containing the services registered by this collection.
        """
        return self._container.build()
