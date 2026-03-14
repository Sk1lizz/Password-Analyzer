"""

"""

class config:

    NAME = "PasswordAnalyzer"
    SETTING = "setting"
    COMMON = "common_file"
    LANG = "language"
    COMMON_FILE = "common"

    FILE_SETTING = "config.json"
    HISTORY_FILE = "history.hist"
    LANGUAGE_FILE = "ru-RU.yaml"

    def __init__(self) -> None:
        pass

    def get_config_path(self) -> dict:
        __config_file = dict()
        __config_file_path = dict()
        __config_file_name = dict()

        __config_file["name"] = self.NAME

        __config_file_path["setting"] = self.SETTING
        __config_file_path["common"] = self.COMMON
        __config_file_path["language"] = self.LANG
        __config_file_path["common-files"] = self.COMMON_FILE

        __config_file_name["setting"] = self.FILE_SETTING
        __config_file_name["history"] = self.HISTORY_FILE
        __config_file_name["language"] = self.LANGUAGE_FILE

        __config_file["path"] = __config_file_path

        __config_file["name_file"] = __config_file_name

        return __config_file