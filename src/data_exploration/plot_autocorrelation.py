import os
import matplotlib.pyplot as plt
from statsmodels.graphics import tsaplots


class PlotAutocorr:

    def __init__(self,
                 dataframe,
                 config,
                 lags=24
                 ):

        self.__plot_acf(
            dataframe=dataframe,
            config=config,
            lags=lags
        )
        self.__plot_pacf(
            dataframe=dataframe,
            config=config,
            lags=lags
        )

    @staticmethod
    def __plot_acf(dataframe,
                   config,
                   lags
                   ):
        fig = tsaplots.plot_acf(
            dataframe[config.dfstructure.close],
            lags=lags,
            fft=True
        )
        plt.title("Autocorrelation")
        fig.savefig(os.path.join(
            *config.dirs2make.figures,
            "Autocorrelation" ".png"
        ))
        plt.close()

    @staticmethod
    def __plot_pacf(dataframe,
                    config,
                    lags
                    ):
        fig = tsaplots.plot_pacf(
            dataframe[config.dfstructure.close],
            lags=lags,
            method="ols"
        )
        plt.title("Partial_Autocorrelation")
        fig.savefig(os.path.join(
            *config.dirs2make.figures,
            "Partial_Autocorrelation" ".png"
        ))
        plt.close()

