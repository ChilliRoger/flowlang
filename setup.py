from setuptools import setup, find_packages

setup(
    name="flowlang",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["flow=flowlang.cli:main"]
    },
)
