# __init__.py

# Importing modules from the package
from app.bendcalc import bend_calc

from .lathecalc import lathe_calc
from .sheetmetalcalc import sheetmetal_calc
from .speedfeed import speed_feed

# Initialization code
print("Initializing my_package...")

# Defining the package's API
__all__ = ['some_function', 'MyClass']
