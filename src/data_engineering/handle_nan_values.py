import pandas as pd
from src.config.load_conifg import Configurator


def count_nan_values(data: pd.DataFrame) -> [int, int, int, int, int]:
    """ Connt the NaN values. """
    nan_amount = [
        f"{col}: {data[col].isna().sum()}"
        for col
        in data.columns
    ]
    return nan_amount


def replace_nan_values(data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """ Replace the NaN values based on predetermined method, set in the configurations. """
    if config.dataengin.fill_method == "polynomial":
        [
            data[col].interpolate(
                method=config.dataengin.fill_method,
                order=config.dataengin.poly_order,
                direction="both",
                inplace=True
            )
            for col
            in data.columns
        ]

    elif config.dataengin.fill_method == "linear":
        [
            data[col].interpolate(
                method=config.dataengin.fill_method,
                direction="both",
                inplace=True
            )
            for col
            in data.columns
        ]

    else:
        raise ValueError("An invalid fill method is given.")

    return data
