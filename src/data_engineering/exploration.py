import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.express as px
from plotly.subplots import make_subplots as mks
from typing import List

from src.plotly_plots.scatter_plot import ScatterTrace

BTC_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\data\\coin_Bitcoin.csv"
ETH_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\data\\coin_Ethereum.csv"
ADA_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\data\\coin_Cardano.csv"
LTC_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\data\\coin_Litecoin.csv"

bitco_df = pd.read_csv(BTC_PATH)
ether_df = pd.read_csv(ETH_PATH)
carda_df = pd.read_csv(ADA_PATH)
litec_df = pd.read_csv(LTC_PATH)


def add_coin_name_in_column_names(df):
    coin_name = df.loc[0, "Symbol"]
    new_cols = [coin_name + "_" + col if col != "Date" else col for col in df.columns]
    df.columns = new_cols
    return df


bitco_df = add_coin_name_in_column_names(bitco_df)
ether_df = add_coin_name_in_column_names(ether_df)
carda_df = add_coin_name_in_column_names(carda_df)
litec_df = add_coin_name_in_column_names(litec_df)


def remove_unused_cols(df):
    unused_col_names = ["SNo", "Name", "Symbol"]
    unused_cols = [[col for col in df.columns if name in col] for name in unused_col_names]
    unused_cols = list(np.concatenate(unused_cols))
    df.drop(columns=unused_cols, axis=1, inplace=True)
    return df


bitco_df = remove_unused_cols(bitco_df)
ether_df = remove_unused_cols(ether_df)
carda_df = remove_unused_cols(carda_df)
litec_df = remove_unused_cols(litec_df)


cryp_df = pd.merge(bitco_df, ether_df, on="Date").merge(
    carda_df, on="Date").merge(
    litec_df, on="Date")


def plot_btc_eth_ltc(df, currencies: List):
    colours = px.colors.qualitative.Plotly
    fig = mks(rows=len(currencies), cols=1)

    for idx, curr in enumerate(currencies):
        fig.add_trace(
            ScatterTrace(
                xdata=df.index,
                ydata=df[curr + "_" + "Close"],
                name=curr,
                linecolour=colours[idx]
            ).trace,
            row=idx + 1,
            col=1
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
    pyo.plot(fig)


plot_btc_eth_ltc(cryp_df, ["BTC", "LTC", "ETH"])

