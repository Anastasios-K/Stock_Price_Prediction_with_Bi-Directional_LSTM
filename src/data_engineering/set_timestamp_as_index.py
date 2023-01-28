class SetIndex:

    def __init__(self,
                 dataframe,
                 config
                 ):
        self.df = self.__set_timestamp_as_index(
            config=config,
            df=dataframe
        )

    @staticmethod
    def __set_timestamp_as_index(config,
                                 df
                                 ):
        df.set_index(
            config.dfstructure.date,
            inplace=True
        )
        return df
