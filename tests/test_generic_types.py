from typing import Generic, List, TypeVar
from taipan_di import DependencyCollection


def test_resolve_generic_types():
    services = DependencyCollection()
    services.register_factory_creator(List[str], lambda provider: ["foo", "bar", "baz"])

    provider = services.build()
    instance = provider.resolve(List[str])
    
def test_resolve_generic_with_alias():
    MyList = List[str]
    
    services = DependencyCollection()
    services.register_factory_creator(MyList, lambda provider: ["foo", "bar", "baz"])
    
    provider = services.build()
    instance = provider.resolve(MyList)
    
def test_resolve_generic_registered_with_alias():
    MyList = List[str]
    
    services = DependencyCollection()
    services.register_factory_creator(MyList, lambda provider: ["foo", "bar", "baz"])
    
    provider = services.build()
    instance = provider.resolve(List[str])
    
    
def test_resolve_custom_generics():
    services = DependencyCollection()
    services.register_factory(MyGenericInterface, MyGenericImplementation)
    
    provider = services.build()
    instance = provider.resolve(MyGenericInterface)


T = TypeVar("T")
class MyGenericInterface(Generic[T]):
    pass

class MyGenericImplementation(MyGenericInterface[str]):
    def __init__(self) -> None:
        super().__init__()