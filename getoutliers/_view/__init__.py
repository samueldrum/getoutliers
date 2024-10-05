import pandas as pd
import numpy as np
from getoutliers._iqr import IQR
import matplotlib.pyplot as plt
from _dtypes.types import Dtype2DOutlier
from _warns.__warnings import view_warning

class ViewOutliers(Dtype2DOutlier):


    # Boxplot method gonna be more flexible in a soon future
    def boxplot(self, save=None):
        """
        Boxplot
        ====

        It gonna show a grafic of your Pandas Series, and it going to return as well a tuple of
        the iqr and median values

        Save
        ---
        You can save the image by doing save="<Path/to/file.png>"
        
        """
        view_warning()
        plt.boxplot(self.data)
        plt.show()
        if save:
            plt.savefig(save)
        iqr = IQR(self.data).theres_outliers(value=True)["value"]
        median = np.median(np.asanyarray(self.data))
        return iqr, median
    
