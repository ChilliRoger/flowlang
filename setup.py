from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flowlang-script",
    version="1.0.1",
    author="ChilliRoger",
    author_email="your.email@example.com",  # Update this
    description="A lightweight interpreted programming language for workflow automation and API orchestration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChilliRoger/flowlang",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
        "Topic :: System :: System Shells",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["flow=flowlang.cli:main"]
    },
    keywords="automation workflow scripting language interpreter api orchestration",
    project_urls={
        "Bug Reports": "https://github.com/ChilliRoger/flowlang/issues",
        "Source": "https://github.com/ChilliRoger/flowlang",
        "Documentation": "https://github.com/ChilliRoger/flowlang/blob/main/README.md",
    },
)
