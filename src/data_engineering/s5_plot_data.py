import os.path
from plotly.subplots import make_subplots as mks
from src.plotly_plots.scatter_plot import ScatterTrace
import matplotlib.colors as mcolors
from typing import List


class PlotData:
    def __init__(self,
                 df,
                 config):
        self.config = config
        self.df = df

        self.layout(df=df,
                      currencies=self.config.currencies.currencies,
                      attributes=[
                          self.config.dfstructure.open,
                          self.config.dfstructure.close,
                          self.config.dfstructure.high,
                          self.config.dfstructure.low
                      ])

    @staticmethod
    def __fig(currencies: List,
              cols: int):
        rows = len(currencies)
        return mks(rows=rows,
                   cols=cols,
                   row_titles=currencies)

    def __traces(self,
                 df,
                 attributes,
                 currencies):
        colours = mcolors.CSS4_COLORS
        fig = self.__fig(currencies=currencies, cols=1)

        color_group = 0
        for idx, curr in enumerate(currencies):
            for attr in attributes:
                fig.add_trace(
                    ScatterTrace(
                        xdata=df[self.config.dfstructure.date],
                        ydata=df[curr + "_" + attr],
                        name=curr + "_" + attr,
                        linecolour=colours[list(colours.keys())[color_group + idx]]
                    ).trace,
                    row=idx + 1,
                    col=1

                )
                color_group += len(currencies)
        return fig

    def layout(self, df, currencies, attributes):
        fig = self.__traces(
            df=df,
            currencies=currencies,
            attributes=attributes
        )
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
        fig.write_html(os.path.join(
            *self.config.dirs2make.figures,
            "Crypto_Currencies.html"
        ))
        if bool(self.config.showfig.showfig):
            fig.show(renderer="browser")
