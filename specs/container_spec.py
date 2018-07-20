from expects import (
    be,
    be_a,
    expect,
    raise_error
)
from mamba import (
    description,
    it
)

from simple_ioc import (
    Container,
    ContainerException
)


class Service(object):
    pass


with description('Container') as self:

    with before.all:
        self.container = Container()

    with it('registers a service'):
        self.container.register('a_service', lambda: Service())

        expect(self.container.get('a_service')).to(be_a(Service))

    with it('disallows registering the same service twice'):
        self.container.register('reserved_identifier', lambda: Service())

        expect(lambda: self.container.register('reserved_identifier', lambda: Service())).to(
            raise_error(ContainerException))

    with it('throws an error when requesting a non registered service'):
        expect(lambda: self.container.get('non_existing')).to(
            raise_error(ContainerException))

    with it('is singleton'):
        another_container = Container()

        expect(self.container).to(be(another_container))
