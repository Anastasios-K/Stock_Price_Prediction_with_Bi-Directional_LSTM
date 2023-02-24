import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics import tsaplots
from src.config.load_conifg import Configurator


class AutocorrPlot:

    def __init__(self,
                 data: pd.DataFrame,
                 config: Configurator):
        print(config.dataexpl.autocorrlag)

        self.__plot_acf(
            data=data,
            config=config)
        # self.__plot_pacf(
        #     dataframe=dataframe,
        #     config=config)

    @staticmethod
    def __plot_acf(data: pd.DataFrame,
                   config: Configurator) -> None:
        fig = tsaplots.plot_acf(
            data[config.dfstructure.close],
            lags=config.dataexpl.autocorrlag,
            fft=True
        )
        plt.title("Autocorrelation")
        fig.savefig(os.path.join(
            *config.dirs2make.figures,
            "Autocorrelation" ".png"
        ))
        plt.close()

    # @staticmethod
    # def __plot_pacf(dataframe: pd.DataFrame,
    #                 config: Config) -> None:
    #     pass
    #     print("pacf")
    #     fig = tsaplots.plot_pacf(
    #         dataframe[config.dfstructure.close],
    #         lags=config.dataexpl.autocorrlag,
    #         method="ols"
    #     )
    #     plt.title("Partial_Autocorrelation")
    #     fig.savefig(os.path.join(
    #         *config.dirs2make.figures,
    #         "Partial_Autocorrelation" ".png"
    #     ))
    #     plt.close()

