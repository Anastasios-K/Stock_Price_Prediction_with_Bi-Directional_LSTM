from typing import List


class SaveReport:

    def __init__(self,
                 data: List,
                 report_name: str = "data_engineering_report.txt",
                 title: str = "Title"):
        self.__write_and_save_txt_report(
            data=data,
            report_name=report_name,
            title=title
        )

    @staticmethod
    def __write_and_save_txt_report(data: List, report_name: str, title: str):
        f = open(report_name, "a")
        f.write(title + "\n")
        f.write("-" * 30 + "\n")
        [f.write(item + "\n") for item in data]
        f.write("-" * 30 + "\n")

        f.close()
