

_active_pandas = False
_dataframe = False


def active_pandas(dataframe):
    """
    Active pandas, Where the dataframe gonna be modificated immediately
    
    """
    global _active_pandas, _dataframe

    _active_pandas = True
    _dataframe = dataframe


def is_pandas_active():

    return _active_pandas