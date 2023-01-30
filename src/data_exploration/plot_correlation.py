import os
import numpy as np
import plotly.graph_objects as go
from src.plotly_plots.heatmap import HeatmapTrace


class CalcCorrel:
    """
    Calculate correlation and Plot heatmap for fully sychronised data (no delays between features)
        corr_method: one of ("pearson", "kendall" or "spearman")
    """

    def __init__(self,
                 dataframe,
                 config,
                 fig_title,
                 corr_method,
                 colorscale="Magma"
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
    def __calc_correlation(dataframe,
                           corr_method
                           ):
        return dataframe.corr(method=corr_method)

    @staticmethod
    def __create_trace(corr_df,
                       colorscale
                       ):
        heatmap_trace = HeatmapTrace(
            data=np.array(corr_df),
            xaxis_vals=corr_df.columns,
            yaxis_vals=corr_df.columns,
            colorscale=colorscale
        )
        return heatmap_trace.trace

    @staticmethod
    def __create_layout(fig_title,
                        config
                        ):
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
    def __create_fig(trace,
                     layout,
                     config,
                     fig_title
                     ):
        fig = go.Figure(
            data=trace,
            layout=layout
        )
        fig.write_html(os.path.join(
            *config.dirs2make.figures,
            fig_title + ".html"
        ))
