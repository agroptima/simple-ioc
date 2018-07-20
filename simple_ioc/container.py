class ContainerException(Exception):
    pass


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Container(object):
    __metaclass__ = _Singleton

    def __init__(self):
        self.__services = {}

    def register(self, identifier, callable):
        if self.__has(identifier):
            raise ContainerException('Identifier already registered: {}'.format(identifier))

        self.__services[identifier] = callable

    def get(self, identifier):
        if not self.__has(identifier):
            raise ContainerException('Identifier not registered: {}'.format(identifier))
        return self.__services[identifier]()

    def __has(self, identifier):
        return identifier in self.__services
