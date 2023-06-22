from taipan_di.classes.dependency_container import DependencyContainer
from taipan_di import TaipanUnregisteredError
from mocks import *

def test_resolve():
    container = DependencyContainer()
    scope = MockScope()

    container.register(MockClass, scope)
    provider = container.build()
    
    instance = provider.resolve(MockClass)

    assert instance is not None
    assert isinstance(instance, MockClass)

def test_resolve_fails_if_not_registered():
    container = DependencyContainer()
    provider = container.build()

    try:
        provider.resolve(MockInterface)
        assert False
    except TaipanUnregisteredError:
        assert True
    except:
        assert False
