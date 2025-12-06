from setuptools import setup, find_packages

setup(
    name="chronos-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "shareddep"   # Only the package name goes here
    ],
)
