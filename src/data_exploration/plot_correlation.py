import os
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from src.plotly_plots.heatmap import HeatmapTrace
from src.config.load_conifg import Configurator


class CorrPlot:
    """ Calculate correlation and Plot heatmap. """

    def __init__(self,
                 data: pd.DataFrame,
                 config: Configurator,
                 unique_id: str,
                 fig_title: str,
                 colorscale: str = "Magma"):

        self.__data = data
        self.__config = config
        self.__unique_id = unique_id
        self.__color = colorscale

        corr = self.__calc_correlation()
        self.__create_fig(
            trace=self.__create_trace(corr_df=corr),
            layout=self.__create_layout(fig_title=fig_title),
            fig_title=fig_title
        )

    def __calc_correlation(self) -> pd.DataFrame:
        return self.__data.corr(method=self.__config.dataexpl.corrmethod)

    def __create_trace(self, corr_df: pd.DataFrame) -> go.Trace:
        heatmap_trace = HeatmapTrace(
            data=np.array(corr_df),
            xaxis_vals=corr_df.columns,
            yaxis_vals=corr_df.columns,
            colorscale=self.__color
        )
        return heatmap_trace.trace

    def __create_layout(self, fig_title: str) -> go.Layout:
        heatmap_layout = go.Layout(
            title=dict(
                font=dict(
                    color=self.__config.plotdefault.title_color,
                    family=self.__config.plotdefault.title_font_style,
                    size=self.__config.plotdefault.title_font_size
                ),
                text=fig_title,
                x=0.5
            )
        )
        return heatmap_layout

    def __create_fig(self,
                     trace: go.Trace,
                     layout: go.Layout,
                     fig_title: str):
        fig = go.Figure(
            data=trace,
            layout=layout
        )
        fig.write_html(os.path.join(
            *self.__config.dirs2make.figures,
            self.__config.modelname.modelname + self.__unique_id,
            fig_title + ".html"
        ))
