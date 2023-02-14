import matplotlib.pyplot as plt
from math import ceil
import itertools
import os


class DistributionPlot:

    def __init__(self,
                 dataframe,
                 config
                 ):
        cols, rows = self.__calc_subplot_rows_cols(dataframe=dataframe)
        self.__create_distr_subplots(
            cols=cols,
            rows=rows,
            dataframe=dataframe,
            config=config
        )

    @staticmethod
    def __calc_subplot_rows_cols(dataframe):
        subplot_cols = 3
        subplot_rows = ceil(len(dataframe.columns) / subplot_cols)
        return subplot_cols, subplot_rows

    @staticmethod
    def __create_distr_subplots(cols,
                                rows,
                                dataframe,
                                config
                                ):
        subplot_coordinates = list(itertools.product(
            range(0, rows),
            range(0, cols)
        ))

        fig, axs = plt.subplots(rows, cols, figsize=(12, 10))

        for idx in range(0, len(dataframe.columns)):
            subplot_coord = subplot_coordinates[idx]
            data_plot = dataframe[dataframe.columns[idx]]

            axs[subplot_coord].hist(
                x=data_plot,
                bins=50,
                density=True,
                facecolor='blue',
                alpha=0.75
            )
            axs[subplot_coord].set_title(dataframe.columns[idx])
            axs[subplot_coord].set_xticks([])
            axs[subplot_coord].set_yticks([])

        plt.close(fig)

        fig.savefig(os.path.join(
            *config.dirs2make.figures,
            "Data_Distribution" ".png"
        ))

