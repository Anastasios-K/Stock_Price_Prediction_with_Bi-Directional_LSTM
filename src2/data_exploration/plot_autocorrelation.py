import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics import tsaplots
from src.config.load_conifg import Config


class AutocorrPlot:

    def __init__(self,
                 dataframe: pd.DataFrame,
                 config: Config,
                 lags: int = 24):

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
    def __plot_acf(dataframe: pd.DataFrame,
                   config: Config,
                   lags: int) -> None:
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
    def __plot_pacf(dataframe: pd.DataFrame,
                    config: Config,
                    lags: int) -> None:
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

