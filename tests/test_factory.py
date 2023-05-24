from taipan import DependencyCollection, TaipanTypeError
from mocks import *


def test_register_factory_succeeds():
    services = DependencyCollection()

    try:
        services.register_factory(MockInterface, MockClass)
        assert True
    except:
        assert False


def test_register_factory_fails():
    services = DependencyCollection()

    try:
        services.register_factory(MockInterface, MockWrongClass)
        assert False
    except TaipanTypeError:
        assert True
    except:
        assert False


def test_resolve_factory():
    services = DependencyCollection()
    services.register_factory(MockInterface, MockClass)

    provider = services.build()
    instance = provider.resolve(MockInterface)

    assert isinstance(instance, MockInterface)
    assert instance is not None
    assert instance != provider.resolve(MockInterface)


def test_resolve_factory_fails_if_no_init():
    services = DependencyCollection()
    services.register_factory(MockInterface, MockClassNoInit)

    provider = services.build()

    try:
        instance = provider.resolve(MockInterface)
        assert False
    except TaipanTypeError:
        assert True
    except:
        assert False


def test_contains_factory():
    services = DependencyCollection()
    services.register_factory(MockInterface, MockClass)

    provider = services.build()

    assert provider.contains(MockInterface)
    assert not provider.contains(MockClass)
    assert not provider.contains(MockWrongInterface)
