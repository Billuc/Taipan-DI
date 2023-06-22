from taipan_di import ServiceCollection, TaipanResolutionError
from mocks import *


def test_register_singleton_succeeds():
    services = ServiceCollection()

    try:
        services.register(MockInterface).as_singleton().with_implementation(MockClass)
        assert True
    except:
        assert False


def test_register_singleton_with_wrong_class_works():
    services = ServiceCollection()
    # There should be an error here in the editor though
    services.register(MockInterface).as_singleton().with_implementation(MockWrongClass)

    provider = services.build()
    instance = provider.resolve(MockInterface)

    assert isinstance(instance, MockWrongClass)
    assert not isinstance(instance, MockInterface)


def test_resolve_singleton():
    services = ServiceCollection()
    services.register(MockInterface).as_singleton().with_implementation(MockClass)

    provider = services.build()
    instance = provider.resolve(MockInterface)

    assert isinstance(instance, MockInterface)
    assert instance is not None
    assert instance == provider.resolve(MockInterface)


def test_resolve_singleton_fails_if_no_init():
    services = ServiceCollection()
    services.register(MockInterface).as_singleton().with_implementation(MockClassNoInit)

    provider = services.build()

    try:
        instance = provider.resolve(MockInterface)
        assert False
    except TaipanResolutionError:
        assert True
    except:
        assert False


def test_contains_singleton():
    services = ServiceCollection()
    services.register(MockInterface).as_singleton().with_implementation(MockClass)

    provider = services.build()

    assert provider.contains(MockInterface)
    assert not provider.contains(MockClass)
    assert not provider.contains(MockWrongInterface)


def test_resolve_singleton_no_interface():
    services = ServiceCollection()
    services.register(MockClass).as_singleton().with_self()

    provider = services.build()
    instance = provider.resolve(MockClass)

    assert provider.contains(MockClass)
    assert isinstance(instance, MockClass)
    assert instance is not None
    assert instance == provider.resolve(MockClass)


def test_doesnt_contain_singleton_if_no_with():
    services = ServiceCollection()
    services.register(MockClass).as_singleton()

    provider = services.build()

    assert not provider.contains(MockClass)
