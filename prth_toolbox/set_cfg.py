

"""
set_cfg.py.py  –  Lightweight PRTH / Z-PRTH toolbox
Author : Anne.V 
"""
# Global configuration dictionary
cfg = {
    'fs': 500,          # Sampling frequency (Hz)
    'window': (-0.25, 0.25),
    'bin_size': 0.015,
    'min_ripples': 2,
    'min_spikes': 1,
    'n_shuffle': 500,
    'n_permutations': 5000,
    'epoch_windows': {
        'Fixation': (0, 1),
        'stim1_offset': (1, 2),
        'WorkingMemory': (2, 3),
        'stim2_offset': (3, 4),
        'DecisionMaking': (4, 5),
        'FullTrial': (0, 5)
    }
}

def set_cfg(**kw):
    """Update the global configuration with provided keyword arguments."""
    cfg.update(kw)
