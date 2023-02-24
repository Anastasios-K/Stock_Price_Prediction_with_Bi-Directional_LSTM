import pandas as pd
from src.data_TA_features.typical_price import typical_price
from src.config.load_conifg import Configurator


def money_flow(data: pd.DataFrame, config: Configurator):
    """ Money Flow (mf) """
    tp = typical_price(
        data=data,
        config=config
    )

    mf = tp * data[config.dfstructure.volume]
    return mf


