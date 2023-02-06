import pandas as pd


class GetData:

    def __init__(self,
                 config):
        self.row_data = pd.read_csv(config.paths.datapath)
