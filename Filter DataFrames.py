'''Filter Rows From DataFrames That Don't Satisfy Condition'''

import pandas as pd

def filter_dataframe(df, col, func):
    if col not in df.columns:
        raise ValueError(f"Column '{col}' is not present in the DataFrame.")
    else:
        df_true = df[df[col].apply(func)]
        df_false = df.drop(df_true.index,axis=0)
    return df_false