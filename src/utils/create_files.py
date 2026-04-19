import platform
from pathlib import Path
import os
import json

import src.utils.language_config as lang_files


"""

"""

config_data = {
    "name": "PasswordAnalyzer",
    "version": "1.0.0",
    "language": "ru-RU",
    "history-amount": "5",
    "theme": "system",
    "common-level": "3"
}

language_data_RU = lang_files.ru_RU

language_data_EN = lang_files.en_EN

language_data_CN = lang_files.zn_CH

common_one = lang_files.one

common_two = lang_files.two

common_three = lang_files.three


history_data = ""

class create_files:

    __name: str # 
    __dir_setting: str # 
    __dir_common: str # 
    __dir_lang: str # 
    __dir_common_files: str # 

    __file_setting: str # 
    __file_history: str # 
    __file_language: str # 

    path_to_config: str # 
    path_to_history: str # 
    path_to_language: str # 
    path_to_common_file: str # 


    def __init__(self, config_dict: dict | None = None) -> None:
        if config_dict is None:
            raise SystemExit("byebye")
        

        #
        self.__name = config_dict["name"]

        # 
        path_dict = config_dict["path"]

        self.__dir_setting = path_dict["setting"]
        self.__dir_common = path_dict["common"]
        self.__dir_lang = path_dict["language"]
        self.__dir_common_files = path_dict["common-files"]

        # 
        name_file_dict = config_dict["name_file"]

        self.__file_setting = name_file_dict["setting"]
        self.__file_history = name_file_dict["history"]
        self.__file_language = name_file_dict["language"]

        return 
    

    def create_file(self) -> bool:
        try:
            name_platform = self.get_platform()

            if name_platform == "Windows":
                path = Path(os.getenv("APPDATA"))
            
            elif name_platform == "Linux":
                xdg_data_home = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
                path = Path(xdg_data_home)
            
            main_path = path / f"{self.__name}"

            path_setting = main_path / f"{self.__dir_setting}"
            path_lang = main_path / f"{self.__dir_lang}"
            path_common = main_path / f"{self.__dir_common}"

            path_common_file = path_common / f"{self.__dir_common_files}"

            path_to_history = path_common / f"{self.__file_history}"
            path_to_lang = path_lang / f"{self.__file_language}"
            path_to_config = path_setting / f"{self.__file_setting}"

            self.path_to_config = path_to_config
            self.path_to_history = path_to_history
            self.path_to_language = path_lang
            self.path_to_common_file = path_common_file

            path_to_lang_en = path_lang / f"en-EN.yaml"
            path_to_lang_cn = path_lang / f"zn-CN.yaml"
            path_to_common_1 = path_common_file / "1.txt"
            path_to_common_2 = path_common_file / "2.txt"
            path_to_common_3 = path_common_file / "3.txt"

            path_to_history.parent.mkdir(parents=True, exist_ok=True)
            path_to_lang.parent.mkdir(parents=True, exist_ok=True)
            path_to_config.parent.mkdir(parents=True, exist_ok=True)

            path_common_file.mkdir(parents=True, exist_ok=True)

            if not path_to_history.exists():
                path_to_history.write_text(data=history_data, encoding="utf-8")

            if not path_to_lang.exists():
                path_to_lang.write_text(data=language_data_RU, encoding="utf-8")

            if not path_to_common_1.exists():
                path_to_common_1.write_text(data=common_one, encoding="utf-8")

            if not path_to_common_2.exists():
                path_to_common_2.write_text(data=common_two, encoding="utf-8")

            if not path_to_common_3.exists():
                path_to_common_3.write_text(data=common_three, encoding="utf-8")

            if not path_to_lang_en.exists():
                path_to_lang_en.write_text(data=language_data_EN, encoding="utf-8")

            if not path_to_lang_cn.exists():
                path_to_lang_cn.write_text(data=language_data_CN, encoding="utf-8")

            if not path_to_config.exists():
                with open(path_to_config, "w", encoding="utf-8") as __file:
                    json.dump(config_data, __file, indent=4, ensure_ascii=False)

            return True

        except:
            return False


    
    def get_platform(self) -> str:
        name_platform = platform.system()

        name = ["Windows", "Linux"]

        if name_platform in name:
            return name_platform
        
        pass


    def get_path(self) -> dict:
        result = dict()

        result["setting"] = str(self.path_to_config).replace("\\", "/")
        result["language"] = str(self.path_to_language).replace("\\", "/")
        result["history"] = str(self.path_to_history).replace("\\", "/")
        result["common"] = str(self.path_to_common_file).replace("\\", "/")

        return result
