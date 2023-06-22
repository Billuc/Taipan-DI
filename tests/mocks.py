from typing import Generic, Type, TypeVar

from taipan_di import TaipanResolutionError, BaseServiceProvider
from taipan_di.interfaces import BaseScope

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


class MockScope:
    def get_instance(self, container: BaseServiceProvider) -> MockClass:
        return MockClass()
