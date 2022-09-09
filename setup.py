
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pathplanning",
    description="Path Planning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aishaouadah/UAV-Path-Planning",
    version="1.0",
    license="MIT",
    author="Aicha OUADAH",
    packages=find_packages(),
    tests_require=["numpy", "pandas"],
    include_package_data=True,
    install_requires=[],
)