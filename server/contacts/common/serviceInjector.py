from functools import wraps

class ServiceInjector:
    deps = {}

    def register(self, name=None):
        name = name

        def decorator(thing):
            if not name:
                if not hasattr(thing, '__name__'):
                    raise Exception('no name')
                thing_name = thing.__name__
            else:
                thing_name = name
            self.__class__.deps[thing_name] = thing
            return thing

        return decorator

    class inject:
        def __init__(self, *args):
            self.selected_deps = args

        def __call__(self, func):
            @wraps(func)
            def decorated(*args, **kwargs):
                selected_deps = {k: v for k, v in ServiceInjector.deps.items() if k in self.selected_deps}
                new_kwargs = {**kwargs, **selected_deps}
                return func(*args, **new_kwargs)

            return decorated