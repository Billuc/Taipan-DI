from typing import Any, Callable, Type, TypeVar, cast

from diip.interfaces import BaseDependencyProvider, BaseScope
from diip.errors import DIIPTypeError

T = TypeVar("T")

class FactoryScope(BaseScope):
    def __init__(self, creator: Callable[[BaseDependencyProvider], Any]) -> None:
        self._creator = creator

    def get_instance(self, type: Type[T], container: BaseDependencyProvider) -> T:
        instance = self._creator(container)

        if not isinstance(instance, type):
            raise DIIPTypeError("Created instance is not of type %s", str(type))

        result = cast(T, instance)
        return result
