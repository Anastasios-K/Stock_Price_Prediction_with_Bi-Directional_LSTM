import os
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from src.plotly_plots.heatmap import HeatmapTrace
from src.config.load_conifg import Config


class CorrPlot:
    """
    Calculate correlation and Plot heatmap for fully sychronised data (no delays between features)
        corr_method: one of ("pearson", "kendall" or "spearman")
    """

    def __init__(self,
                 dataframe: pd.DataFrame,
                 config: Config,
                 fig_title: str,
                 corr_method: str,
                 colorscale: str = "Magma"
                 ):

        corr = self.__calc_correlation(
            dataframe=dataframe,
            corr_method=corr_method
        )
        trace = self.__create_trace(
            corr_df=corr,
            colorscale=colorscale
        )
        layout = self.__create_layout(
            fig_title=fig_title,
            config=config
        )
        self.__create_fig(
            trace=trace,
            layout=layout,
            config=config,
            fig_title=fig_title
        )

    @staticmethod
    def __calc_correlation(dataframe: pd.DataFrame,
                           corr_method: str) -> pd.DataFrame:
        return dataframe.corr(method=corr_method)

    @staticmethod
    def __create_trace(corr_df: pd.DataFrame,
                       colorscale: str) -> go.Trace:
        heatmap_trace = HeatmapTrace(
            data=np.array(corr_df),
            xaxis_vals=corr_df.columns,
            yaxis_vals=corr_df.columns,
            colorscale=colorscale
        )
        return heatmap_trace.trace

    @staticmethod
    def __create_layout(fig_title: str,
                        config: Config) -> go.Layout:
        heatmap_layout = go.Layout(
            title=dict(
                font=dict(
                    color=config.plotdefault.title_color,
                    family=config.plotdefault.title_font_style,
                    size=config.plotdefault.title_font_size
                ),
                text=fig_title,
                x=0.5
            )
        )
        return heatmap_layout

    @staticmethod
    def __create_fig(trace: go.Trace,
                     layout: go.Layout,
                     config: Config,
                     fig_title: str):
        fig = go.Figure(
            data=trace,
            layout=layout
        )
        fig.write_html(os.path.join(
            *config.dirs2make.figures,
            fig_title + ".html"
        ))
