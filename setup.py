from setuptools import setup, find_packages

setup(
    name="chronos-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "git+https://github.com/mahmoudediem/shareddep.git@v3.0.0#egg=shareddep"
    ],
)