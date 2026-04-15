import platform
from pathlib import Path
import os
import json


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

language_data_RU = '''# Языковой файл для Password Analyzer
# Версия: 1.0.0
# Язык: Русский

meta:
  language: "Русский"
  code: "ru-RU"
  author: "skilizz"
  version: "1.0.0"
  last_update: "15.04.2026"


# ==========================================================
# =================== Основные надписи =====================
# ==========================================================


app:
  name: "PasswordAnalyzer"
  title: "🔐 Анализатор паролей 🔐"
  waiting-message: "Введите пароль..."
  result-text: "Результат: "

  full-text: "📊 Детальный анализ:"
  text-result-full: 
    len: "Длина: <len> <suffix>"
    len-suffix:
      0: "символ"
      1: "символа"
      2: "символов"
    upper: "Заглавные буквы: A-Z"
    lower: "Строчные буквы: a-z"
    number: "Цифры: 0-9"
    special: "Спецсимволы: !@#$%"
    entropy: "Энтропия: <entropy> бит"

    liked-password: "Схожесть с популярными паролями: "
    result-liked: "Статус: <status>"
    result-liked-password:
      0: "Отсутствует"
      1: "Похож"
      2: "Точное совпадение"
    if-liked: "Пароль похож на"

    power-password: "💪 Надёжность: "
  
  status-text: 
    -1: "Ошибка"        
    0: "Ужасный пароль"               
    1: "Очень плохой пароль"
    2: "Плохой пароль"
    3: "Нормальный пароль"
    4: "Хороший пароль"
    5: "Отличный пароль"
    6: "Превосходный пароль"
    7: "Самый защищённый пароль"
  
  status:
    -1: "ОШИБКА"
    0: "УЖАСНО"
    1: "УЖАСНО"
    2: "ПЛОХО"
    3: "НОРМАЛЬНО"
    4: "ХОРОШИЙ"
    5: "ОТЛИЧНО"
    6: "ОТЛИЧНО"
    7: "ПРЕВОСХОДНО"

  button-text:
    setting: "⚙️ Настройки"
    generate: "🎲 Генерация"
    history: "📜 История"
    show-password: "🔓 Показать пароль"
    hide-password: "🔒 Скрыть пароль"
    copy: "📋 Скопировать"
    successful-copy: "✅ Скопировано!"

setting:
  name: "PasswordAnalyzer - settings"
  title: "Настройки"
  title-theme: "Тема оформления:"
  theme:
    light: "Светлая"
    dark: "Тёмная"
    system: "Как в системе"
  title-history: "Максимум записей в истории:"
  title-language: "Язык:"
  waiting-message: "Выберите язык"
  button-save: "Сохранить изменения"
  successful-save: "✅ Настройки применены!"
  

generate:
  name: "PasswordAnalyzer - generate"
  title: "🔐 Генератор паролей 🔐"
  button:
    generate: "🎲 Генерация"
    setting: "⚙️ Настройки"
    main-app: "🔐 Анализатор"
    history: "📜 История"
    copy: "📋 Скопировать"
    successful-copy: "✅ Скопировано!"

  text-result-full:
    len: "<len> симв."
    upper: "Использовать заглавные буквы"
    lower: "Использовать строчные буквы"
    custom: "Использовать русские буквы"
    number: "Использовать числа"
    special: "Использовать спецсимволы"
    error: "❌ Невозможно сгенерировать пароль"'''


language_data_EN = '''# Language file for Password Analyzer
# Version: 1.0.0
# Language: English

meta:
  language: "English"
  code: "en-EN"
  author: "skilizz"
  version: "1.0.0"
  last_update: "15.04.2026"


# ==========================================================
# =================== Main Labels ==========================
# ==========================================================


app:
  name: "PasswordAnalyzer"
  title: "🔐 Password Analyzer 🔐"
  waiting-message: "Enter password..."
  result-text: "Result: "

  full-text: "📊 Detailed analysis:"
  text-result-full: 
    len: "Length: <len> <suffix>"
    len-suffix:
      0: "character"
      1: "characters"
      2: "characters"
    upper: "Uppercase letters: A-Z"
    lower: "Lowercase letters: a-z"
    number: "Digits: 0-9"
    special: "Special characters: !@#$%"
    entropy: "Entropy: <entropy> bits"

    liked-password: "Similarity to common passwords: "
    result-liked: "Status: <status>"
    result-liked-password:
      0: "None"
      1: "Similar"
      2: "Exact match"
    if-liked: "Password is similar to"

    power-password: "💪 Strength: "
  
  status-text: 
    -1: "Error"        
    0: "Terrible password"               
    1: "Very bad password"
    2: "Bad password"
    3: "Normal password"
    4: "Good password"
    5: "Excellent password"
    6: "Superb password"
    7: "Most secure password"
  
  status:
    -1: "ERROR"
    0: "TERRIBLE"
    1: "TERRIBLE"
    2: "BAD"
    3: "NORMAL"
    4: "GOOD"
    5: "EXCELLENT"
    6: "EXCELLENT"
    7: "SUPERB"

  button-text:
    setting: "⚙️ Settings"
    generate: "🎲 Generate"
    history: "📜 History"
    show-password: "🔓 Show password"
    hide-password: "🔒 Hide password"
    copy: "📋 Copy"
    successful-copy: "✅ Copied!"

setting:
  name: "PasswordAnalyzer - settings"
  title: "Settings"
  title-theme: "Theme:"
  theme:
    light: "Light"
    dark: "Dark"
    system: "System default"
  title-history: "Max history entries:"
  title-language: "Language:"
  waiting-message: "Select language"
  button-save: "Save changes"
  successful-save: "✅ Settings applied!"
  

generate:
  name: "PasswordAnalyzer - generate"
  title: "🔐 Password Generator 🔐"
  button:
    generate: "🎲 Generate"
    setting: "⚙️ Settings"
    main-app: "🔐 Analyzer"
    history: "📜 History"
    copy: "📋 Copy"
    successful-copy: "✅ Copied!"

  text-result-full:
    len: "<len> chars"
    upper: "Use uppercase letters"
    lower: "Use lowercase letters"
    custom: "Use Russian letters"
    number: "Use numbers"
    special: "Use special characters"
    error: "❌ Cannot generate password"'''

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

            path_to_history.parent.mkdir(parents=True, exist_ok=True)
            path_to_lang.parent.mkdir(parents=True, exist_ok=True)
            path_to_config.parent.mkdir(parents=True, exist_ok=True)

            path_common_file.mkdir(parents=True, exist_ok=True)

            if not path_to_history.exists():
                path_to_history.write_text(data=history_data, encoding="utf-8")

            if not path_to_lang.exists():
                path_to_lang.write_text(data=language_data_RU, encoding="utf-8")

            if not path_to_lang_en.exists():
                path_to_lang_en.write_text(data=language_data_EN, encoding="utf-8")

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
