from typing import List, Union
import os


class SaveReport:

    def __init__(self,
                 path2save: Union,
                 data: List,
                 report_name: str = "data_engineering_report.txt",
                 title: str = "Title"):
        self.__write_and_save_txt_report(
            path2save=path2save,
            data=data,
            report_name=report_name,
            title=title
        )

    @staticmethod
    def __write_and_save_txt_report(path2save: List, data: List, report_name: str, title: str):
        path = os.path.join(*path2save)
        os.makedirs(path, exist_ok=True)
        f = open(os.path.join(path, report_name), "a")
        f.write(title + "\n")
        f.write("-" * 30 + "\n")
        [f.write(item + "\n") for item in data]
        f.write("-" * 30 + "\n")
        f.close()
