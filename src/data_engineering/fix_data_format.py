import pandas as pd
from src.config.load_conifg import Configurator


def fix_data_format(raw_data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """
    Fix data format and data types. So, data is ready for engineering, analysis etc.
    Set timestamp as index.
    Drop Adj Close feature.
    """
    if config.dfstructure.date not in raw_data.columns:
        raise ValueError("Data does not have Date feature")
    if config.dfstructure.close not in raw_data.columns:
        raise ValueError("Data does not have Close feature")
    if config.dfstructure.open not in raw_data.columns:
        raise ValueError("Data does not have Open feature")
    if config.dfstructure.high not in raw_data.columns:
        raise ValueError("Data does not have High feature")
    if config.dfstructure.low not in raw_data.columns:
        raise ValueError("Data does not have Low feature")
    if config.dfstructure.volume not in raw_data.columns:
        raise ValueError("Data does not have Volume feature")

    for col in raw_data.columns:
        if col == config.dfstructure.date:
            raw_data[col] = pd.to_datetime(raw_data[col])
        else:
            raw_data[col] = pd.to_numeric(raw_data[col])

    raw_data.set_index(
        config.dfstructure.date,
        inplace=True
    )
    if config.dfstructure.adjclose in raw_data.columns:
        raw_data.drop(
            columns=[config.dfstructure.adjclose],
            inplace=True
        )

    fixed_data = raw_data.copy()
    return fixed_data
