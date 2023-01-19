import plotly.offline as pyo
from plotly.subplots import make_subplots as mks
from src.plotly_plots.scatter_plot import ScatterTrace
import matplotlib.colors as mcolors


class PlotData:
    def __init__(self,
                 df,
                 attributes,
                 currencies):

        self.__layout(
            df=df,
            currencies=currencies,
            attributes=attributes)

    @staticmethod
    def __fig(rows, cols):
        return mks(rows=rows, cols=cols)

    def __traces(self,
                 df,
                 attributes,
                 currencies):
        colours = mcolors.CSS4_COLORS
        fig = self.__fig(rows=len(currencies), cols=1)

        color_group = 0
        for idx, curr in enumerate(currencies):
            for attr in attributes:
                fig.add_trace(
                    ScatterTrace(
                        xdata=df["Date"],
                        ydata=df[curr + "_" + attr],
                        name=curr + "_" + attr,
                        linecolour=colours[list(colours.keys())[color_group + idx]]
                    ).trace,
                    row=idx + 1,
                    col=1

                )
                color_group += 4
        return fig

    def __layout(self, df, currencies, attributes):
        fig = self.__traces(df=df, currencies=currencies, attributes=attributes)
        fig.update_layout(
            plot_bgcolor="#D0D0CE",
            title=dict(
                font=dict(
                    color="#000000",
                    family="Arial",
                    size=20
                ),
                text="Crypto Currencies",
                x=0.5
            ),
        )
        fig.update_xaxes(
            showline=True,
            linewidth=2,
            linecolor="#000000"
        )
        fig.update_yaxes(
            showline=True,
            linewidth=2,
            linecolor="#000000"
        )
        pyo.plot(fig)
