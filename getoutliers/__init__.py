"""

get out, liers😅
=======
Outliers it's just a library to identify outliers in a pandas Dataframe and manipulate them

'Made by Samuel'

"""

__all__ = ["detecting",
           "manipulating",
           "nan_value",
           "active_pandas",
           "is_pandas_active"
           ]

__version__ = "0.0.5.1"


from . import detecting, manipulating
from ._nan_value import nan_value
from . import api



