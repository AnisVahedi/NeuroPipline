
import numpy as np
from prth_toolbox.set_cfg import cfg

def get_bins() -> np.ndarray:
    w0, w1 = cfg['window']
    bs = cfg['bin_size']
    return np.arange(w0, w1 + bs, bs)
