# My Package

A simple calculator package for demonstration purposes.

## Installation

```bash
pip install my_package
```

## Usage
```
from my_package.calculator import Calculator

calc = Calculator()
print(calc.add(1, 2))  # Output: 3
```

### Build the Package

To build the package, run the following commands in the root directory of your project:

```bash
python setup.py sdist bdist_wheel
```

### Publishing
Install twine if you haven't already:
```
pip install twine
```
Upload your package to TestPyPI to test the upload process:
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
Once you're satisfied with the upload to TestPyPI, upload your package to the main PyPI:
```
twine upload dist/*
```
### Install the Package
```
pip install my_package
```
