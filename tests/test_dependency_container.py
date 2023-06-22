from typing import cast
from taipan_di.classes.service_container import ServiceContainer
from taipan_di.classes.service_provider import ServiceProvider
from taipan_di.errors.taipan_unregistered_error import TaipanUnregisteredError
from mocks import *


def test_init_container():
    container = ServiceContainer()

    assert len(container._services) == 0
    assert not container.contains(MockInterface)
    assert not container.contains(MockClass)


def test_register():
    container = ServiceContainer()
    service = MockScope()

    container.register(MockClass, service)

    assert container._services == {MockClass: service}


def test_contains():
    container = ServiceContainer()
    service = MockScope()

    container.register(MockClass, service)

    assert container.contains(MockClass)
    assert not container.contains(MockInterface)
    assert not container.contains(MockWrongClass)


def test_provider_has_same_services():
    container = ServiceContainer()
    service = MockScope()

    container.register(MockClass, service)
    provider = cast(ServiceProvider, container.build())

    assert provider._services == container._services
