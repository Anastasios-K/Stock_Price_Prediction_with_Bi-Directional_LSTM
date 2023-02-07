import pandas as pd


class TP:
    """ Typical Price """

    def __init__(self,
                 dataframe: pd.DataFrame,
                 config
                 ):
        self.typical_price = self.__typical_price(
            df=dataframe,
            config=config
        )

    @staticmethod
    def __typical_price(df,
                        config
                        ):
        typical_price = (
                df[config.dfstructure.close] +
                df[config.dfstructure.high] +
                df[config.dfstructure.low]
        ) / 3

        return typical_price
