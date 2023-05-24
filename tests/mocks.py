from typing import Type, TypeVar

from taipan import TaipanTypeError, BaseDependencyProvider
from taipan.interfaces import BaseScope

T = TypeVar("T")


class MockInterface:
    pass


class MockClass(MockInterface):
    def __init__(self) -> None:
        super().__init__()


class MockClassNoInit(MockInterface):
    pass


class MockWrongInterface:
    pass


class MockWrongClass(MockWrongInterface):
    def __init__(self) -> None:
        super().__init__()


class MockScope(BaseScope):
    def get_instance(self, type: Type[T], container: BaseDependencyProvider) -> T:
        if not issubclass(MockClass, type):
            raise TaipanTypeError("Instance is not of type %s", str(type))

        return MockClass()
