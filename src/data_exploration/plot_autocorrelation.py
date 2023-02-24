import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics import tsaplots
from src.config.load_conifg import Configurator


class AutocorrPlot:

    def __init__(
            self,
            data: pd.DataFrame,
            config: Configurator,
            unique_id: str
    ):
        self.__data = data
        self.__config = config
        self.__unique_id = unique_id

        self.__plot_acf()
        self.__plot_pacf()

    def __plot_acf(self) -> None:
        fig = tsaplots.plot_acf(
            self.__data[self.__config.dfstructure.close],
            lags=self.__config.dataexpl.autocorrlag,
            fft=True
        )
        plt.title("Autocorrelation")
        fig.savefig(os.path.join(
            *self.__config.dirs2make.figures,
            self.__config.modelname.modelname + self.__unique_id,
            "Autocorrelation" ".png"
        ))
        plt.close()

    def __plot_pacf(self) -> None:
        pass
        print("pacf")
        fig = tsaplots.plot_pacf(
            self.__data[self.__config.dfstructure.close],
            lags=self.__config.dataexpl.autocorrlag,
            method="ols"
        )
        plt.title("Partial_Autocorrelation")
        fig.savefig(os.path.join(
            *self.__config.dirs2make.figures,
            self.__config.modelname.modelname + self.__unique_id,
            "Partial_Autocorrelation" ".png"
        ))
        plt.close()

