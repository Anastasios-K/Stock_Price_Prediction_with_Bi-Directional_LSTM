import pandas as pd
from src.config.load_conifg import Configurator


def set_date_index(data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """ Create a Date feature. Gets Date from index, as it is set in the "fixed data types/foramt" step. """
    data[config.dfstructure.date] = data.index
    return data


def count_duplicates(data: pd.DataFrame, config: Configurator) -> int:
    """ Count duplicates based on the Date feature. """
    data = set_date_index(data=data, config=config)
    dupli_amount = data[config.dfstructure.date].duplicated(False).sum()
    return dupli_amount


def remove_duplicates(data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """ Remove duplicates identified based on the Date feature. Drops the Date feature at the end. """
    data = set_date_index(data=data, config=config)
    data.drop_duplicates(
        subset="Date",
        keep="first",
        inplace=True
    )
    data.drop(
        columns=[config.dfstructure.date],
        inplace=True
    )
    return data
