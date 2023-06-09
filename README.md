# Taipan-DI

Truly Amazing Inversion of control Python library Analogous to .Net's DI

Taipan-DI is a [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection) library whose goal is to provide a behaviour similar to [.Net's DI system](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection).


## Features

 - Lightweight
 - No decorators
 - No hidden behaviour (what you write is what you get)
 - Automatic dependency injection on service resolving
 - Type hinting
 - No global container by default
 - Singleton and factory scopes
 - Register pipelines easily


## Constraints

 - Based purely on types (not on strings)
 - No automatic registration


## Installation

### Pip

> `pip install taipan-di`

### Poetry

[Poetry](https://python-poetry.org/) is a Python dependency management and packaging tool. I actually use it for this project.

> `poetry add taipan-di`


## Usage

First, you have to create a `ServiceCollection` in which you will register your services. Each `ServiceCollection` is independant and contain different services.

```python
services = ServiceCollection()
```

Then, register your services as you wish. You can initiate registrations processes via 2 ways :

```python
services.register(Type)
services.register_pipeline(Type)
```

For "standard" registration, you have to first choose the scope and then how you wish the instances to be created. Examples :

```python
services.register(Type).as_factory().with_implementation(ChildType)
services.register(Type).as_singleton().with_self()
services.register(Type).as_singleton().with_instance(instance)
services.register(Type).as_factory().with_creator(lambda provider: create(provider))
```

For pipeline registration, all you have to do is add the links that constitute the pipeline and register it as a singleton or a factory. Example :

```python
services.register_pipeline(Type).add(Link1).add(Link2).as_factory()
```

Once your services are registered, you have to build a service provider which will be used to resolve services : 

```python
provider = services.build()
resolved = provider.resolve(Type)
```

If `Type` has a constructor dependency, it will be automatically resolved, as long as the dependency has been registered in the `ServiceCollection`.


## Inspirations

This library is partially based on the [*kink*](https://pypi.org/project/kink/) dependency injection library. I was using kink on another project previously but it didn't fit all my requirements and wishes.

I also took inspiration from the [*injector*](https://pypi.org/project/injector/) library and .Net's dependency injection system.


## TODO

This library isn't stable yet and a lot of things can still be improved.
If there is something you want to see added or if something does not work as you want it to, feel free to open an issue.

Here is a list of features I have in mind and will be working on :

 - Create configuration from environment or configuration files

