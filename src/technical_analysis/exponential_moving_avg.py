class EMA:
    """ Exponential Moving Average """

    def __init__(self,
                 close_price,
                 rolling_window: int = 12
                 ):

        self.ema = self.__exponential_moving_avg(
            price=close_price,
            rolling_window=rolling_window
        )

    @staticmethod
    def __exponential_moving_avg(price,
                                 rolling_window
                                 ):
        ema = price.ewm(
            span=rolling_window,
            adjust=False
        ).mean()
        return ema