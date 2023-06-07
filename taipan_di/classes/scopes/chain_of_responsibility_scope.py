from typing import Any, Callable, List, Type, TypeVar, cast

from taipan_di.interfaces import BaseDependencyProvider, BaseScope

from taipan_di.classes.tools import ChainOfResponsibilityFactory

T = TypeVar("T")

class ChainOfResponsibilityScope(BaseScope):
    def __init__(self, creators: List[Callable[[BaseDependencyProvider], Any]]) -> None:
        self._creators = creators

    def get_instance(self, type: Type[T], container: BaseDependencyProvider) -> T:
        factory = ChainOfResponsibilityFactory()
        
        for creator in self._creators:
            factory.add(creator(container))
            
        chain_of_responsibility = factory.build()
        result = cast(type, chain_of_responsibility)
        return result
