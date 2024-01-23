import numpy as np


def access_circular(arr, index):
    array_length = len(arr)
    circular_index = index % array_length
    return arr[circular_index]

