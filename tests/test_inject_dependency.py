from taipan_di.classes.service_collection import ServiceCollection


def test_inject_dependency():
    services = ServiceCollection()
    inner = MockInner()
    
    services.register(MockInner).as_singleton().with_instance(inner)
    services.register(MockOuter).as_factory().with_self()
    
    provider = services.build()
    outer_1 = provider.resolve(MockOuter)
    outer_2 = provider.resolve(MockOuter)
    
    assert outer_1 is not None
    assert outer_2 is not None
    assert outer_1._inner is not None
    assert outer_2._inner is not None
    assert outer_1 != outer_2
    assert outer_1._inner == outer_2._inner == inner


class MockInner:
    def __init__(self) -> None:
        self._name = "John Doe"

class MockOuter:
    def __init__(self, inner: MockInner) -> None:
        self._inner = inner