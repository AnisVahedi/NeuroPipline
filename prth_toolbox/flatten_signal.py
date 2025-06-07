
import numpy as np
from collections.abc import Sequence

def flatten_signal(x) -> np.ndarray:
    """
    Flatten nested lists/arrays into a 1-D numpy float32 array.
    """
    if isinstance(x, (list, tuple)):
        rows = x
    elif isinstance(x, np.ndarray):
        rows = x.tolist()
    else:
        raise TypeError(f"Cannot interpret {type(x)} as signal container")
    flat = []
    for r in rows:
        flat.extend(r.tolist() if hasattr(r, 'tolist') else (r if isinstance(r, Sequence) else [r]))
    arr = np.array(flat, dtype=np.float32).squeeze()
    if arr.ndim != 1:
        raise ValueError("flatten_signal produced non-1D output")
    return arr
