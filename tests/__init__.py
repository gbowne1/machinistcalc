# __init__.py

# Importing modules from the package
from .module1 import some_function
from .module2 import MyClass

# Initialization code
print("Initializing my_package...")

# Defining the package's API
__all__ = ['some_function', 'MyClass']
