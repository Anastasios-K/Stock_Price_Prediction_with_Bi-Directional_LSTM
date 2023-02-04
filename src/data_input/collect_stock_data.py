import pandas as pd


class GetData:

    def __init__(self,
                 config):
        self.data = pd.read_csv(config.paths.datapath)
