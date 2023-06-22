from taipan_di import DependencyCollection, TaipanResolutionError
from mocks import *


def test_register_factory_succeeds():
    services = DependencyCollection()

    try:
        services.register(MockInterface).as_factory().with_implementation(MockClass)
        assert True
    except:
        assert False


def test_register_factory_with_wrong_class_works():
    services = DependencyCollection()
    # There should be an error here in the editor though
    services.register(MockInterface).as_factory().with_implementation(MockWrongClass)

    provider = services.build()
    instance = provider.resolve(MockInterface)

    assert isinstance(instance, MockWrongClass)
    assert not isinstance(instance, MockInterface)


def test_resolve_factory():
    services = DependencyCollection()
    services.register(MockInterface).as_factory().with_implementation(MockClass)

    provider = services.build()
    instance = provider.resolve(MockInterface)

    assert isinstance(instance, MockInterface)
    assert instance is not None
    assert instance != provider.resolve(MockInterface)


def test_resolve_factory_fails_if_no_init():
    services = DependencyCollection()
    services.register(MockInterface).as_factory().with_implementation(MockClassNoInit)

    provider = services.build()

    try:
        instance = provider.resolve(MockInterface)
        assert False
    except TaipanResolutionError:
        assert True
    except:
        assert False


def test_contains_factory():
    services = DependencyCollection()
    services.register(MockInterface).as_factory().with_implementation(MockClass)

    provider = services.build()

    assert provider.contains(MockInterface)
    assert not provider.contains(MockClass)
    assert not provider.contains(MockWrongInterface)


def test_resolve_factory_no_interface():
    services = DependencyCollection()
    services.register(MockClass).as_factory().with_self()

    provider = services.build()
    instance = provider.resolve(MockClass)

    assert provider.contains(MockClass)
    assert isinstance(instance, MockClass)
    assert instance is not None
    assert instance != provider.resolve(MockClass)


def test_doesnt_contain_factory_if_no_with():
    services = DependencyCollection()
    services.register(MockClass).as_factory()

    provider = services.build()

    assert not provider.contains(MockClass)
