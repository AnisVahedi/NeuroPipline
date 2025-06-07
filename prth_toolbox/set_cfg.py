
cfg = {
    'fs': 500,
    'window': (-0.25, 0.25),
    'bin_size': 0.02,
    'min_ripples': 2,
    'min_spikes':0,
    'n_shuffle': 500,
    'n_permutations': 5000,
    'epoch_windows': {
        'fix': (0, 1),
        'stim1_offset': (1, 2),
        'WorkingMemory': (2, 3),
        'stim2_offset': (3, 4),
        'DecisionMaking': (4, 5),
    }
}

def set_cfg(**kw):
    cfg.update(kw)
