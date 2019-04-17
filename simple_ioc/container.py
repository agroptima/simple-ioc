class ContainerException(Exception):
    pass


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Container(object, metaclass=_Singleton):
    def __init__(self):
        self.__locators = {}
        self.__instances = {}

    def register(self, identifier, callable):
        if self.__has(identifier):
            raise ContainerException('Identifier already registered: {}'.format(identifier))

        self.__locators[identifier] = callable

    def get(self, identifier):
        if not self.__has(identifier):
            raise ContainerException('Identifier not registered: {}'.format(identifier))

        return self.__instance_of(identifier)

    def __has(self, identifier):
        return identifier in self.__locators

    def __instance_of(self, identifier):
        if identifier not in self.__instances:
            self.__instances[identifier] = self.__locators[identifier]()

        return self.__instances[identifier]
