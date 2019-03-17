from setuptools import setup, find_packages

setup(
    name="comprehension-server",
    packages=find_packages(),
    install_requires=[
        "falcon"
    ],
    entry_points={
        "console_scripts": [
        ]
    }
)

