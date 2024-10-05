import warnings


class NotImplemented(Warning):
    pass


def zscore_warning():
    warnings.warn("Zscore class is not recommended to use, Because it is not really well implemented, use IQR class instead.", NotImplemented)


def manipulate2D():
    warnings.warn("The ManiOut2D class is not well implemented for manipulating DataFrames. "
            "Please use the ManiOut1D class and the 'active_pandas' API for direct manipulation of the original DataFrame. "
            "Example usage:\n"
            "```python\n"
            "import pandas as pd\n"
            "from getoutliers.api import active_pandas, ManiOut1D\n\n"
            "# Load your DataFrame\n"
            "df = pd.DataFrame({'column1': [1, 2, 3], 'column2': [4, 5, 6]})\n\n"
            "# Activate direct manipulation\n"
            "active_pandas(df)\n\n"
            "# Now you can use ManiOut1D for outlier manipulation\n"
            "manipulator = ManiOut1D(df)\n"
            "manipulator.remove_outliers()\n"
            "```", NotImplemented)
    

def iqrmultid():
    warnings.warn("The IqrMultiD class does not work well for detecting outliers in a DataFrame. "
            "Please use the IQR class instead for more reliable results. "
            "Example usage:\n"
            "```python\n"
            "import pandas as pd\n"
            "from getoutliers.detecting import IQR\n\n"
            "# Load your DataFrame\n"
            "df = pd.DataFrame({'column1': [1, 2, 3, 100], 'column2': [4, 5, 6, 200]})\n\n"
            "# Create an instance of the IQR class\n"
            "outlier_detector = IQR(df)\n\n"
            "# Detect outliers in the DataFrame\n"
            "outliers = outlier_detector.theres_outliers()\n\n"
            "# View the detected outliers\n"
            "print(outliers)\n"
            "```", NotImplemented)