from setuptools import setup, find_packages

setup(
    name="vuln-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask==1.0",
        "requests==2.19.0",
        "urllib3==1.24.1",
        "PyYAML==5.1"
    ],
)