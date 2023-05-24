from diip.classes.dependency_container import DependencyContainer
from diip import DIIPUnregisteredError
from mocks import *

def test_resolve():
    container = DependencyContainer()
    service = MockScope()

    container.register(MockClass, service)
    provider = container.build()
    
    instance = provider.resolve(MockClass)

    assert instance is not None
    assert isinstance(instance, MockClass)

def test_resolve_fails():
    container = DependencyContainer()
    provider = container.build()

    try:
        provider.resolve(MockInterface)
        assert False
    except DIIPUnregisteredError:
        assert True
    except:
        assert False
