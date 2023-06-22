from dataclasses import dataclass

from taipan_di.classes import ServiceCollection


def test_register_with_dataclasses():
    services = ServiceCollection()
    inner = MockInner("John Doe")
    
    services.register(MockInner).as_singleton().with_instance(inner)
    services.register(MockOuter).as_factory().with_self()
    
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