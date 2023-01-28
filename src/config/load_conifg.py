from dataclasses import dataclass
import typing as t
from src.secondary_modules.read_yaml import YamlReader


@dataclass
class Currencies:
    currencies: str

    @classmethod
    def read_config(cls: t.Type["Currencies"], obj: dict):
        return cls(
            currencies=obj["crypto_currencies"]
        )


@dataclass
class FileType:
    datafiletype: str

    @classmethod
    def read_config(cls: t.Type["FileType"], obj: dict):
        return cls(
            datafiletype=obj["data_files_type"]
        )


@dataclass
class DfStructure:
    date: str
    name: str
    symbol: str
    close: str
    open: str
    high: str
    low: str
    marketplace: str
    serialID: str

    @classmethod
    def read_config(cls: t.Type["DfStructure"], obj: dict):
        return cls(
            date=obj["df_structure"]["date"],
            name=obj["df_structure"]["name"],
            symbol=obj["df_structure"]["symbol"],
            close=obj["df_structure"]["close"],
            open=obj["df_structure"]["open"],
            high=obj["df_structure"]["high"],
            low=obj["df_structure"]["low"],
            marketplace=obj["df_structure"]["marketcap"],
            serialID=obj["df_structure"]["serialID"]
        )


@dataclass
class Paths:
    datapath: str

    @classmethod
    def read_config(cls: t.Type["Paths"], obj: dict):
        return cls(
            datapath=obj["paths"]["data_path"]
        )


@dataclass
class Dirs2Make:
    reports: str
    figures: str
    models: str
    best_models: str

    @classmethod
    def read_config(cls: t.Type["Dirs2Make"], obj: dict):
        return cls(
            reports=obj["required_dirs"]["reports"],
            figures=obj["required_dirs"]["figures"],
            models=obj["required_dirs"]["models"],
            best_models=obj["required_dirs"]["best_models"]
        )


@dataclass
class Feature2Shift:
    feature2shift: str

    @classmethod
    def read_config(cls: t.Type["Feature2Shift"], obj: dict):
        return cls(
            feature2shift=obj["feature2shift"]
        )


class Config:

    def __init__(self, config_path):
        config_file = YamlReader(path=config_path).content

        self.currencies = Currencies.read_config(obj=config_file)
        self.datafiletype = FileType.read_config(obj=config_file)
        self.dfstructure = DfStructure.read_config(obj=config_file)
        self.paths = Paths.read_config(obj=config_file)
        self.dirs2make = Dirs2Make.read_config(obj=config_file)
        self.feature2shift = Feature2Shift.read_config(obj=config_file)
