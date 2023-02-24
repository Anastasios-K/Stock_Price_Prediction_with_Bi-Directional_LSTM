import matplotlib.pyplot as plt
from math import ceil
import itertools
import os
import pandas as pd
from src.config.load_conifg import Configurator


def calc_subplot_rows_cols(data: pd.DataFrame) -> (int, int):
    subplot_cols = 3
    subplot_rows = ceil(len(data.columns) / subplot_cols)
    return subplot_cols, subplot_rows


def create_distr_subplots(data: pd.DataFrame,
                          config: Configurator,
                          unique_id: str,
                          file_name: str) -> None:
    cols, rows = calc_subplot_rows_cols(data=data)

    subplot_coordinates = list(itertools.product(
        range(0, rows),
        range(0, cols)
    ))

    fig, axs = plt.subplots(rows, cols, figsize=(12, 10))

    for idx in range(0, len(data.columns)):
        subplot_coord = subplot_coordinates[idx]
        data_plot = data[data.columns[idx]]

        axs[subplot_coord].hist(
            x=data_plot,
            bins=50,
            density=True,
            facecolor='blue',
            alpha=0.75
        )
        axs[subplot_coord].set_title(data.columns[idx])
        axs[subplot_coord].set_xticks([])
        axs[subplot_coord].set_yticks([])

    plt.close(fig)

    fig.savefig(os.path.join(
        *config.dirs2make.figures,
        config.modelname.modelname + unique_id,
        file_name + ".png"
    ))

