from src.plotly_plots.scatter_plot import ScatterTrace
import plotly.graph_objects as go
import os
import pandas as pd


class DataResolutionPlot:

    def __init__(self,
                 data: pd.DataFrame,
                 config,
                 fig_title
                 ):
        self.cooked_data = self.__plot_moving_avgs(
            data=data,
            config=config,
            title=fig_title
        )

    @staticmethod
    def __calc_weekly_resolution(data):
        return data.resample('W').mean()

    @staticmethod
    def __calc_monthly_resolution(data):
        return data.resample('M').mean()

    @staticmethod
    def __calc_seasonal_resolution(data):
        return data.resample('3M').mean()

    @staticmethod
    def __calc_quarter_resolution(data):
        return data.resample('Q').mean()

    @staticmethod
    def __calc_yearly_resolution(data):
        return data.resample('Y').mean()

    def __plot_moving_avgs(self,
                           data: pd.DataFrame,
                           config,
                           title
                           ):
        weeek = self.__calc_weekly_resolution(data=data)
        month = self.__calc_monthly_resolution(data=data)
        season = self.__calc_seasonal_resolution(data=data)
        quarter = self.__calc_quarter_resolution(data=data)
        year = self.__calc_yearly_resolution(data=data)

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

        return data
