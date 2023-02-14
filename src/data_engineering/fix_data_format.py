import pandas as pd
from src.config.load_conifg import Config
from src.secondary_modules.report_saving import ReportSaving


def fix_data_format(raw_data: pd.DataFrame, config: Config) -> pd.DataFrame:
    """ Fix data format and data types. So, data is ready for engineering, analysis etc. """

    for col in raw_data.columns:
        if col == config.dfstructure.date:
            raw_data[col] = pd.to_datetime(raw_data[col])

            raw_data.set_index(
                config.dfstructure.date,
                inplace=True
            )

        else:
            raw_data[col] = pd.to_numeric(raw_data[col])

    fixed_data = raw_data.copy()

    # prepare list for reporting
    types = fixed_data.dtypes
    attributes = list(types.index)
    types = list(types)

    reporting_list = [
        attr + " - " + str(localtype)
        for attr, localtype
        in zip(attributes, types)
    ]
    ReportSaving(
        data=reporting_list,
        title="Dtypes",
        path2save=config.dirs2make.reports
    )
    return fixed_data
