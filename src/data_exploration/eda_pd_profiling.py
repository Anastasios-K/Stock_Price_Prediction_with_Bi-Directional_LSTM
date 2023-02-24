import os
import pandas as pd
from pandas_profiling import ProfileReport
from src.config.load_conifg import Configurator


def create_eda_report(data: pd.DataFrame,
                      config: Configurator,
                      unique_id: str,
                      report_name: str) -> None:
    profile = ProfileReport(
        data,
        tsmode=True,
        sortby=config.dfstructure.date
    )
    profile.to_file(os.path.join(
        *config.dirs2make.figures,
        config.modelname.modelname + unique_id,
        report_name + ".html"
    ))
