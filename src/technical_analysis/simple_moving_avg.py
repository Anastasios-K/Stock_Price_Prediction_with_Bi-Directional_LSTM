class SMA:
    """ Simple Moving Average """

    def __init__(self,
                 close_price,
                 rolling_window: int = 30
                 ):

        self.sma = self.__simple_movinge_avg(
            close_price=close_price,
            rolling_window=rolling_window
        )

    @staticmethod
    def __simple_movinge_avg(close_price,
                             rolling_window
                             ):
        sma = close_price.rolling(rolling_window).mean()
        return sma
