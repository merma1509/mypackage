from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude='tests*'),
    license='MIT',
    description="Mugabo First Package Example",
    long_description=open("README.md").read(),
    author="Mugabo",
    author_email="mugabo15@theopenclimate.com",
    url="https://github.com/mugabo/mypackage",
    install_requires=["numpy"],
    
)