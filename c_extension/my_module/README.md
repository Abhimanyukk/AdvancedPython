# C Extension module build instructions
## Build the C extension
Run the following command to build the extension:
```
python setup.py build
```

This will generate a shared object file (.so on Linux/Mac, .pyd on Windows) in a build directory. 

## Install the module to use anywhere
To install the module so you can use it in your Python environment, run:
```
python setup.py install
```