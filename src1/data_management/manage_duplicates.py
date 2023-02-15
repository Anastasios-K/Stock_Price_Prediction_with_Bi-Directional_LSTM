import pandas as pd
from src.secondary_modules.report_saving import ReportSaving
from src.data_engineering.handle_duplicates import DataWithoutDuplicates
from src.data_management.data_management import FixedDTypeData
from src.data_management.data_management import NoDuplicateData


def manage_duplicates(obj: FixedDTypeData):
    print("kanw handle ta duplicates")

    data = obj.fixed_dtype_data
    configuration = obj.config

    def __set_date_index():
        data[configuration.dfstructure.date] = data.index
        return data

    def __count_duplicates():
        new_data = __set_date_index()
        path2save = configuration.dirs2make.reports
        dupli_amount = new_data[configuration.dfstructure.date].duplicated(False).sum()

        ReportSaving(
            path2save=path2save,
            data=list(str(dupli_amount)),
            title="Duplicates"
        )

    def __remove_duplicates() -> pd.DataFrame:
        new_data = __set_date_index()
        new_data.drop_duplicates(
            subset="Date",
            keep="first",
            inplace=True
        )
        new_data.drop(
            columns=[configuration.dfstructure.date],
            inplace=True
        )
        return new_data

    __count_duplicates()
    no_dupl_data_obj = NoDuplicateData()
    no_dupl_data_obj.config = configuration
    no_dupl_data_obj.no_dupl_data = __remove_duplicates()

    return no_dupl_data_obj
