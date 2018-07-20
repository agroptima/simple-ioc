# Simple IoC

[![Build Status](https://travis-ci.org/agroptima/simple-ioc.png)](https://travis-ci.org/agroptima/simple-ioc)
[![License GPLv3](https://img.shields.io/badge/license-GPLv3-red.svg)](https://opensource.org/licenses/GPL-3.0)
![Python versions](https://img.shields.io/badge/python-2.7-blue.svg)

## Install

```
$ pipenv install simple-ioc
```

or

```
$ pip install simple-ioc
```

## Usage

In order to have the IoC (Inversion of Control) working in your application, you must register your services in the IoC container:

```python
from simple_ioc import Container

class AService(object):
    # Your service implementation comes here

Container().register('an_identifier', lambda: AService())
```

Then, from any point in your application, you can retrieve the service by calling `get`:

```python
a_service = Container().get('an_identifier')
```
