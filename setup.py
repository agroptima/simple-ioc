from setuptools import setup


setup(
    name="simple-ioc",
    version="3.2.0",
    license="GPLv3",
    author="Isagri S.L.U.",
    author_email="devs.es@groupeisagri.com",
    description="A lightweight library with an implementation of IoC",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/agroptima/simple-ioc",
    download_url="https://github.com/agroptima/simple-ioc/releases",
    keywords=["python", "dependency-injection", "inversion-of-control"],
    packages=["simple_ioc"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
