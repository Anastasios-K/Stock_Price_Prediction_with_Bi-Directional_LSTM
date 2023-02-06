from src.plotly_plots.scatter_plot import ScatterTrace
import plotly.graph_objects as go
import os
import pandas as pd
from src.data_engineering.handle_data_types import HandleDataTypes


class DataResolution:

    def __init__(self,
                 row_data: pd.DataFrame,
                 config,
                 fig_title
                 ):
        dataframe = HandleDataTypes(
            row_data=row_data,
            config=config
        ).cooked_data

        self.cooked_data = self.__plot_moving_avgs(
            cooked_data=dataframe,
            config=config,
            title=fig_title
        )

    @staticmethod
    def __calc_weekly_resolution(cooked_data):
        return cooked_data.resample('W').mean()

    @staticmethod
    def __calc_monthly_resolution(cooked_data):
        return cooked_data.resample('M').mean()

    @staticmethod
    def __calc_seasonal_resolution(cooked_data):
        return cooked_data.resample('3M').mean()

    @staticmethod
    def __calc_quarter_resolution(cooked_data):
        return cooked_data.resample('Q').mean()

    @staticmethod
    def __calc_yearly_resolution(cooked_data):
        return cooked_data.resample('Y').mean()

    def __plot_moving_avgs(self,
                           cooked_data: pd.DataFrame,
                           config,
                           title
                           ):
        weeek = self.__calc_weekly_resolution(cooked_data=cooked_data)
        month = self.__calc_monthly_resolution(cooked_data=cooked_data)
        season = self.__calc_seasonal_resolution(cooked_data=cooked_data)
        quarter = self.__calc_quarter_resolution(cooked_data=cooked_data)
        year = self.__calc_yearly_resolution(cooked_data=cooked_data)

        week_trace = ScatterTrace(
            xdata=weeek.index,
            ydata=weeek[config.dfstructure.close],
            name="weekly_resolution",
            mode="lines",
            linecolour="#046A38"
        ).trace
        month_trace = ScatterTrace(
            xdata=month.index,
            ydata=month[config.dfstructure.close],
            name="month_resolution",
            mode="lines",
            linecolour="#C4D600"
        ).trace
        season_trace = ScatterTrace(
            xdata=season.index,
            ydata=season[config.dfstructure.close],
            name="season_resolution",
            mode="lines",
            linecolour="#00A3E0"
        ).trace
        quarter_trace = ScatterTrace(
            xdata=quarter.index,
            ydata=quarter[config.dfstructure.close],
            name="quarter_resolution",
            mode="lines",
            linecolour="#75787B"
        ).trace
        year_trace = ScatterTrace(
            xdata=year.index,
            ydata=year[config.dfstructure.close],
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
                season_trace,
                quarter_trace,
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

        return cooked_data
