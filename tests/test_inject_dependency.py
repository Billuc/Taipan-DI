from diip.classes.dependency_collection import DependencyCollection


def test_inject_dependency():
    services = DependencyCollection()
    inner = MockInner()
    
    services.register_singleton_instance(MockInner, inner)
    services.register_factory(MockOuter, MockOuter)
    
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