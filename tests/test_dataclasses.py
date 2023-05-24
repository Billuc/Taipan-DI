from dataclasses import dataclass

from diip.classes import DependencyCollection


def test_register_with_dataclasses():
    services = DependencyCollection()
    inner = MockInner("John Doe")
    
    services.register_singleton_instance(MockInner, inner)
    services.register_factory(MockOuter, MockOuter)
    
    provider = services.build()
    outer_1 = provider.resolve(MockOuter)
    outer_2 = provider.resolve(MockOuter)
    
    assert outer_1 == outer_2
    assert id(outer_1) != id(outer_2)
    assert outer_1._inner == outer_2._inner == inner

@dataclass
class MockInner:
    _name: str
        
@dataclass
class MockOuter:
    _inner: MockInner