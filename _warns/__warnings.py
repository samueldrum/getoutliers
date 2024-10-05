import warnings


class NotImplemented(Warning):
    pass

def view_warning():
    warnings.warn("""This boxplot function is not fully implemented. It is recommended to use Matplotlib for better visualization.""", NotImplemented)


def zscore_warning():
    warnings.warn("Zscore class is not recommended to use, Because it is not really well implemented, use IQR class instead.")