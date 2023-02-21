import plotly.graph_objects as go


class HeatmapTrace:

    def __init__(self,
                 data,
                 xaxis_vals,
                 yaxis_vals,
                 colorscale
                 ):
        self.trace = go.Heatmap(z=data,
                                y=yaxis_vals,
                                x=xaxis_vals,
                                colorscale=colorscale)


