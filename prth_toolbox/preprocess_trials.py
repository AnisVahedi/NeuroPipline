
import numpy as np
import pandas as pd
from prth_toolbox.flatten_signal import flatten_signal
from prth_toolbox.set_cfg import cfg
def preprocess_trials(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process trial DataFrame: add 'monkey', 'label_perf', 'area_group',
    'ReactionTime', 'RT_category', and flatten 'spike','fire','cleanSig'.
    Then keep only rows meeting ripple/spike criteria.
    """
    df = df.copy()

    df['monkey'] = df['Filename'].str.extract(r'^(ADR|ELV|NIN)')[0]
    df['label_perf'] = df.groupby('monkey')['Perf']         .transform(lambda s: (s >= s.median()).astype(int))
    df['area_group'] = np.where(df.Area.isin([1,2]), 'ventral', 'dorsal')
    df['ReactionTime'] = df['Reward_onT_values'] - df['Target_onT_values']
    df['RT_category'] = df.groupby(['FilenameGroup','monkey'])['ReactionTime']         .transform(lambda x: pd.qcut(x, 2, labels=['fast','slow'], duplicates='drop'))
    for c in ['spike','fire','cleanSig']:
        if c in df.columns:
            df[c] = df[c].apply(flatten_signal)
    def apply_keep_criteria(row):
        spikes = row['spike']
        rips = row['ripple_events']
        rip_times = [r[0] for r in rips if r[0] >= 500]
        return (len(rip_times) >= cfg['min_ripples']
                and np.sum(spikes[500:]) >= cfg['min_spikes'])
    return df[df.apply(apply_keep_criteria, axis=1)].reset_index(drop=True)

