
import numpy as np
import typing as _t
from prth_toolbox.set_cfg import cfg
from prth_toolbox.get_bins import get_bins

def _hist(st: np.ndarray, rt: float, bins) -> np.ndarray:
    return np.histogram(st - rt, bins)[0]

def compute_prth(st: np.ndarray, rt: _t.Sequence[float]) -> np.ndarray:
    bins = get_bins()
    if len(rt) == 0:
        return np.zeros(len(bins) - 1, dtype=float)
    return np.mean([_hist(st, r, bins) for r in rt], axis=0)

def compute_zprth(st: np.ndarray, rt: _t.Sequence[float], n: int | None = None) -> np.ndarray:
    n = n or cfg['n_shuffle']
    real = compute_prth(st, rt) / cfg['bin_size']
    null = np.zeros((n, len(real)))
    T = 6.0
    for i in range(n):
        fake_rt = np.random.uniform(0, T, len(rt))
        null[i] = compute_prth(st, fake_rt) / cfg['bin_size']
    mu = null.mean(axis=0)
    sigma = null.std(axis=0)
    z = (real - mu) / (sigma + 1e-6)
    return np.clip(z, -10, 10).tolist()
