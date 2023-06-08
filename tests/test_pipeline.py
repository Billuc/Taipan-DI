from typing import Callable
from taipan_di import DependencyCollection, PipelineLink

BaseGreetingProvider = PipelineLink[str, str]



class NameProvider(BaseGreetingProvider):
    def _handle(self, request: str, next: Callable[[str], str]) -> str:
        name = request if request is not None else "World"
        
        return next(name) or name
        

class SalutationAdder(BaseGreetingProvider):
    def _handle(self, request: str, next: Callable[[str], str]) -> str:
        greeting = "Hi " + request
        
        return next(greeting) or greeting


class SuffixAdder(BaseGreetingProvider):
    def _handle(self, request: str, next: Callable[[str], str]) -> str:
        greeting = request + ", how are you ?"
        
        return next(greeting) or greeting
    

class AdminDetector(BaseGreetingProvider):
    def _handle(self, request: str, next: Callable[[str], str]) -> str:
        if request == "admin":
            return "Oh hi admin ! What can I do for you ?"
        
        return next(request)


def test_register_pipeline():
    services = DependencyCollection()
    services.register_pipeline(BaseGreetingProvider)\
        .add(NameProvider)\
        .add(SalutationAdder)\
        .add(SuffixAdder)\
        .register()

    provider = services.build()
    assert provider.contains(BaseGreetingProvider)


def test_not_contained_if_not_registered():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseGreetingProvider)\
        .add(NameProvider)\
        .add(SalutationAdder)\
        .add(SuffixAdder)\

    provider = services.build()
    assert not provider.contains(BaseGreetingProvider)
    
    
def test_resolve_pipeline():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseGreetingProvider)\
        .add(NameProvider)\
        .add(SalutationAdder)\
        .add(SuffixAdder)\
        .register()

    provider = services.build()
    instance = provider.resolve(BaseGreetingProvider)
    
    assert instance is not None
    assert instance != provider.resolve(BaseGreetingProvider)
    
    
def test_resolve_pipeline_as_singleton():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseGreetingProvider, True)\
        .add(NameProvider)\
        .add(SalutationAdder)\
        .add(SuffixAdder)\
        .register()

    provider = services.build()
    instance = provider.resolve(BaseGreetingProvider)
    
    assert instance is not None
    assert instance == provider.resolve(BaseGreetingProvider)
    
    
def test_pipeline_exec():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseGreetingProvider)\
        .add(NameProvider)\
        .add(SalutationAdder)\
        .add(SuffixAdder)\
        .register()

    provider = services.build()
    instance = provider.resolve(BaseGreetingProvider)
    
    assert instance.exec("John") == "Hi John, how are you ?"
    assert instance.exec(None) == "Hi World, how are you ?"
    
    
def test_exit_link():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseGreetingProvider)\
        .add(AdminDetector)\
        .add(NameProvider)\
        .register()
        
    provider = services.build()
    instance = provider.resolve(BaseGreetingProvider)
    
    assert instance.exec("admin") == "Oh hi admin ! What can I do for you ?"
    assert instance.exec("John") == "John"
    assert instance.exec(None) == "World"