from typing import Generic, List, TypeVar
from taipan_di import DependencyCollection


def test_resolve_generic_types():
    services = DependencyCollection()
    services.register(List[str]).as_factory().with_creator(
        lambda provider: ["foo", "bar", "baz"]
    )

    provider = services.build()
    instance = provider.resolve(List[str])


def test_resolve_generic_with_alias():
    MyList = List[str]

    services = DependencyCollection()
    services.register(MyList).as_factory().with_creator(
        lambda provider: ["foo", "bar", "baz"]
    )

    provider = services.build()
    instance = provider.resolve(MyList)


def test_resolve_generic_registered_with_alias():
    MyList = List[str]

    services = DependencyCollection()
    services.register(MyList).as_factory().with_creator(
        lambda provider: ["foo", "bar", "baz"]
    )

    provider = services.build()
    instance = provider.resolve(List[str])


def test_resolve_custom_generics():
    services = DependencyCollection()
    services.register(MyGenericInterface).as_factory().with_implementation(
        MyGenericImplementation
    )

    provider = services.build()
    instance = provider.resolve(MyGenericInterface)


def test_resolve_custom_generics_with_type():
    services = DependencyCollection()
    services.register(MyGenericInterface[str]).as_factory().with_implementation(
        MyGenericImplementation
    )

    provider = services.build()
    instance = provider.resolve(MyGenericInterface[str])


T = TypeVar("T")


class MyGenericInterface(Generic[T]):
    pass


class MyGenericImplementation(MyGenericInterface[str]):
    def __init__(self) -> None:
        super().__init__()
