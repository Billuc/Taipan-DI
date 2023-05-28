from taipan_di import DependencyCollection, TaipanTypeError
from mocks import *


def test_register_singleton_succeeds():
    services = DependencyCollection()

    try:
        services.register_singleton(MockInterface, MockClass)
        assert True
    except:
        assert False


def test_register_singleton_fails():
    services = DependencyCollection()

    try:
        services.register_singleton(MockInterface, MockWrongClass)
        assert False
    except TaipanTypeError:
        assert True
    except:
        assert False


def test_resolve_singleton():
    services = DependencyCollection()
    services.register_singleton(MockInterface, MockClass)

    provider = services.build()
    instance = provider.resolve(MockInterface)

    assert isinstance(instance, MockInterface)
    assert instance is not None
    assert instance == provider.resolve(MockInterface)


def test_resolve_singleton_fails_if_no_init():
    services = DependencyCollection()
    services.register_singleton(MockInterface, MockClassNoInit)

    provider = services.build()

    try:
        instance = provider.resolve(MockInterface)
        assert False
    except TaipanTypeError:
        assert True
    except:
        assert False


def test_contains_singleton():
    services = DependencyCollection()
    services.register_singleton(MockInterface, MockClass)

    provider = services.build()

    assert provider.contains(MockInterface)
    assert not provider.contains(MockClass)
    assert not provider.contains(MockWrongInterface)
    
    
def test_resolve_singleton_no_interface():
    services = DependencyCollection()
    services.register_singleton(MockClass)
    
    provider = services.build()
    instance = provider.resolve(MockClass)
    
    assert provider.contains(MockClass)
    assert isinstance(instance, MockClass)
    assert instance is not None
    assert instance == provider.resolve(MockClass)
