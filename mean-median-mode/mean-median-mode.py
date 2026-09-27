from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    freq = Counter(x.flat)
    
    result = {
        'mean': float(np.mean(x)),
        'median' : float(np.median(x)),
        'mode': float(max(freq, key=freq.get)),
    }

    return result
    