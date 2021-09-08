import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from scipy.ndimage.interpolation import zoom
arr = np.random.uniform(size=(4,4))
arr = zoom(arr, 8)
arr = arr > 0.5
arr = np.where(arr, '-', '#')
arr = np.array_str(arr, max_line_width=500)
print(arr)