from typing import cast
from taipan_di.classes.dependency_container import DependencyContainer
from taipan_di.classes.dependency_provider import DependencyProvider
from taipan_di.errors.taipan_unregistered_error import TaipanUnregisteredError
from mocks import *


def test_init_container():
    container = DependencyContainer()

    assert len(container._services) == 0
    assert not container.contains(MockInterface)
    assert not container.contains(MockClass)


def test_register():
    container = DependencyContainer()
    service = MockScope()

    container.register(MockClass, service)

    assert container._services == {MockClass: service}


def test_contains():
    container = DependencyContainer()
    service = MockScope()

    container.register(MockClass, service)

    assert container.contains(MockClass)
    assert not container.contains(MockInterface)
    assert not container.contains(MockWrongClass)


def test_provider_has_same_services():
    container = DependencyContainer()
    service = MockScope()

    container.register(MockClass, service)
    provider = cast(DependencyProvider, container.build())

    assert provider._services == container._services
