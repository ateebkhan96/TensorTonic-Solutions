import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    N = len(y_pred)

    sub_sq = (np.subtract(y_pred, y_true)) ** 2


    sum = np.sum(sub_sq)


    return float(sum/N)