from taipan_di import DependencyCollection, ChainOfResponsibilityLink

BaseResponder = ChainOfResponsibilityLink[str, str]


class Responder1(BaseResponder):
    def handle(self, request: str) -> str:
        if not request == "foo":
            return super().handle(request)

        return "bar"


class Responder2(BaseResponder):
    def handle(self, request: str) -> str:
        if not request == "hi":
            return super().handle(request)

        return "hello"


class Responder3(BaseResponder):
    def handle(self, request: str) -> str:
        if not request == "ping":
            return super().handle(request)

        return "pong"
    

class Responder4(BaseResponder):
    def handle(self, request: str) -> str:
        if not request == "hi":
            return super().handle(request)

        return "howdy"


def test_register_chain_of_responsibility():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseResponder)\
        .add(Responder1)\
        .add(Responder2)\
        .add(Responder3)\
        .register()

    provider = services.build()
    assert provider.contains(BaseResponder)


def test_not_contained_if_not_registered():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseResponder)\
        .add(Responder1)\
        .add(Responder2)\
        .add(Responder3)\

    provider = services.build()
    assert not provider.contains(BaseResponder)
    
    
def test_resolve_chain_of_responsibility():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseResponder)\
        .add(Responder1)\
        .add(Responder2)\
        .add(Responder3)\
        .register()

    provider = services.build()
    instance = provider.resolve(BaseResponder)
    
    assert instance is not None
    assert instance != provider.resolve(BaseResponder)
    
    
def test_resolve_chain_of_responsibility_as_singleton():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseResponder, True)\
        .add(Responder1)\
        .add(Responder2)\
        .add(Responder3)\
        .register()

    provider = services.build()
    instance = provider.resolve(BaseResponder)
    
    assert instance is not None
    assert instance == provider.resolve(BaseResponder)
    
    
def test_chain_of_responsibility_handle():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseResponder)\
        .add(Responder1)\
        .add(Responder2)\
        .add(Responder3)\
        .register()

    provider = services.build()
    instance = provider.resolve(BaseResponder)
    
    assert instance.handle("foo") == "bar"
    assert instance.handle("hi") == "hello"
    assert instance.handle("ping") == "pong"
    assert instance.handle("idk") == None
    
    
def test_only_one_link_handles_the_request():
    services = DependencyCollection()
    services.register_chain_of_responsibility(BaseResponder)\
        .add(Responder2)\
        .add(Responder4)\
        .register()
        
    provider = services.build()
    instance = provider.resolve(BaseResponder)
    
    assert instance.handle("hi") == "hello"
