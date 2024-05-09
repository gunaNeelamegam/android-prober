from setuptools import setup
from setuptools import find_namespace_packages
from pathlib import Path
from os import path
from sys import version_info

current_path = Path(__file__).parent
full_path = path.join(current_path, "README.md")
long_discription = ""
version = "0.1.3"
name = "android-prober"
description = "Library for test android api's via service"
author = "GunaNeelamegam"
url = "https://github.com/gunaNeelamegam"

with open(full_path) as fd:
    long_discription = fd.read()

excludes = [
    "examples",
]

setup(
    name=name,
    version=version,
    description=description,
    license = "Apacher License 2.0",
    url= url,
    author= author,
    author_email="gunag77730@gmail.com",
    long_description= long_discription,
    packages= find_namespace_packages(exclude = excludes),
    long_description_content_type= "text/markdown",
    py_modules = ["android_prober"],
    install_requires = ["flask","kivy", "oscpy", "plyer", "swagger-gen", "pyjnius==1.6.1"]
)


