from setuptools import setup, find_packages

setup(
    name="discord-extras",
    version="0.1.0",
    description="Extra utilities for discord.py",
    author="ValkPy",
    packages=find_packages(),
    install_requires=[
        "discord.py>=2.3.0"
    ],
    python_requires=">=3.8",
)
