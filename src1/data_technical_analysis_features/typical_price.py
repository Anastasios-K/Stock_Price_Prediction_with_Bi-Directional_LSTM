import pandas as pd


class TP:
    """ Typical Price """

    def __init__(self,
                 data: pd.DataFrame,
                 config
                 ):
        self.typical_price = self.__typical_price(
            data=data,
            config=config
        )

    @staticmethod
    def __typical_price(data,
                        config
                        ):
        typical_price = (
                data[config.dfstructure.close] +
                data[config.dfstructure.high] +
                data[config.dfstructure.low]
        ) / 3

        return typical_price
