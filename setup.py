import setuptools
import genet_models
from glob import glob

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
    
VERSION = genet_models.__version__

setuptools.setup(
    name            = "genet_models",
    version         = VERSION,
    author          = "Goosang Yu",
    author_email    = "gsyu93@gmail.com",
    description     = "Models for prediction modules in GenET",
    url             = "https://github.com/Goosang-Yu/genet_models.git",
    packages        = setuptools.find_packages(exclude = ['dev_ing', 'dev_ing.*']),
    
    python_requires = ">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX"
    ],
    
    long_description = long_description,
    long_description_content_type = "text/markdown",
    project_urls={"Bug Tracker": "https://github.com/Goosang-Yu/genet/issues"},
    
    include_package_data=True,
)