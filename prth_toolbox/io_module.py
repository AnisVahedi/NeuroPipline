
import json
from pathlib import Path
import pandas as pd
from prth_toolbox.set_cfg import cfg
def load_data(path: str) -> pd.DataFrame:
    """
    Load a DataFrame from .parquet, .csv, or .feather file.
    """
    p = Path(path)
    if p.suffix == '.parquet':
        return pd.read_parquet(p, engine='pyarrow')
    if p.suffix == '.csv':
        return pd.read_csv(p)
    if p.suffix == '.feather':
        return pd.read_feather(p)
    raise ValueError(f"Unknown file type {p}")

def save_df(df: pd.DataFrame, path: str):
    """
    Save DataFrame to a parquet file with zstd compression and write cfg to .json.
    """

    path = Path(path)
    df.to_parquet(path, compression='zstd')
    with open(path.with_suffix('.json'), 'w') as f:
        json.dump(cfg, f, indent=2)
