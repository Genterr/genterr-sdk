from setuptools import setup, find_packages

setup(
    name="genterr_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp==3.9.1",
        "pydantic==2.5.2",
        "python-dotenv==1.0.0",
        "PyYAML==6.0.1",
    ],
    author="Genterr",
    description="A simple toolkit for creating AI agents on the GENTERR platform",
    python_requires=">=3.9",
)