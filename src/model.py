import numpy as np
import time


class Model:
    """Rotate an array by 90 degrees.

    Args:
        array (np.array): Input numpy array.
        k (Int): Number of times the array is rotated by 90 degrees.
    """
    def __call__(self, array, k=1):
        return np.rot90(array, k)
