import plotly.graph_objects as go
import os
import pandas as pd
from src.config.load_conifg import Configurator
from src.plotly_plots.scatter_plot import ScatterTrace


class DataOverview:
    """ Create and save a plot of different resolutions of the given data. """

    def __init__(self,
                 data: pd.DataFrame,
                 config: Configurator):
        self.__data = data
        self.__config = config

    def __resample_2_weekly(self) -> pd.DataFrame:
        """ Resample data into weekly resolution. """
        return self.__data.resample('W').mean()

    def __resample_2_monthly(self) -> pd.DataFrame:
        """ Resample data into monthly resolution. """
        return self.__data.resample('M').mean()

    def __resample_2_fiscal_quarter(self) -> pd.DataFrame:
        return self.__data.resample('BQ').mean()

    def __resample_2_yearly(self) -> pd.DataFrame:
        return self.__data.resample('Y').mean()

    def plot_all_resolutions(self, title: str) -> None:
        config = self.__config
        y_feature = self.__config.dfstructure.close
        weeek = self.__resample_2_weekly()
        month = self.__resample_2_monthly()
        quarter = self.__resample_2_fiscal_quarter()
        year = self.__resample_2_yearly()

        week_trace = ScatterTrace(
            xdata=weeek.index,
            ydata=weeek[y_feature],
            name="weekly_resolution",
            mode="lines",
            linecolour="#046A38"
        ).trace
        month_trace = ScatterTrace(
            xdata=month.index,
            ydata=month[y_feature],
            name="month_resolution",
            mode="lines",
            linecolour="#C4D600"
        ).trace
        fiscal_quarter_trace = ScatterTrace(
            xdata=quarter.index,
            ydata=quarter[y_feature],
            name="quarter_resolution",
            mode="lines",
            linecolour="#75787B"
        ).trace
        year_trace = ScatterTrace(
            xdata=year.index,
            ydata=year[y_feature],
            name="year_resolution",
            mode="lines",
            linecolour="#ED8B00"
        ).trace

        layout = go.Layout(
            title=dict(
                font=dict(
                    color=config.plotdefault.title_color,
                    family=config.plotdefault.title_font_style,
                    size=config.plotdefault.title_font_size
                ),
                text=title,
                x=0.5
            ),
            xaxis_title=dict(text="Time"),
            yaxis_title=dict(text="Prise"),
        )

        fig = go.Figure(
            data=[
                week_trace,
                month_trace,
                fiscal_quarter_trace,
                year_trace
            ],
            layout=layout
        )

        fig.update_xaxes(
            showline=True,
            linewidth=config.plotdefault.axes_line_width,
            linecolor=config.plotdefault.axes_line_color
        )

        fig.update_yaxes(
            showline=True,
            linewidth=config.plotdefault.axes_line_width,
            linecolor=config.plotdefault.axes_line_color
        )

        fig.write_html(os.path.join(
            *config.dirs2make.figures,
            title + ".html"
        ))
