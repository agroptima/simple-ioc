# Simple IoC

[![Build Status](https://travis-ci.org/agroptima/simple-ioc.svg)](https://travis-ci.org/agroptima/simple-ioc)
[![License GPLv3](https://img.shields.io/badge/license-GPLv3-red.svg)](https://opensource.org/licenses/GPL-3.0)
![Python versions](https://img.shields.io/badge/python-3.x-blue.svg)

## Install

```sh
pipenv install simple-ioc
```

or

```sh
pip install simple-ioc
```

## Usage

In order to have the IoC (Inversion of Control) working in your application, you must register your services in the IoC container:

```python
from simple_ioc import Container

class AService:
    # Your service implementation comes here

Container().register('an_identifier', lambda: AService())
```

Then, from any point in your application, you can retrieve the service by calling `get`:

```python
a_service = Container().get('an_identifier')
```

## Publishing to PyPI

Follow these steps to publish a new version of the package to PyPI:

1. **Update the version number** in `setup.py`

2. **Install build tools** (if not already installed):

   ```sh
   pip install build twine
   ```

3. **Build the distribution packages**:

   ```sh
   python setup.py sdist
   ```

   This creates both source distribution (.tar.gz) and wheel (.whl) in the `dist/` directory.

4. **Verify the build**:

   ```sh
   twine check dist/*
   ```

5. **Upload to PyPI** using twine:

   ```sh
   twine upload dist/*
   ```

   **Note**: Use an API token instead of username/password. Configure it in `~/.pypirc`:

   ```ini
   [pypi]
   username = __token__
   password = pypi-YOUR-API-TOKEN-HERE
   ```

6. **Clean up** the build artifacts (optional):

   ```sh
   rm -rf build/ dist/ *.egg-info/
   ```

### Best Practices

- **Use version tags**: After publishing, tag the release in git:

  ```sh
  git tag -a X.Y.Z -m "Release X.Y.Z"
  git push origin --tags
  ```

### Prerequisites

- You need a PyPI account with the appropriate permissions to upload this package
