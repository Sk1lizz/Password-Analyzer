import json

"""

"""

class edit_data:

    path_to_config: str
    path_to_history: str
    path_to_language: str
    path_to_common_files: str

    def __init__(self, dict_path: dict | None = None) -> None:
        self.path_to_config = dict_path["setting"]
        self.path_to_history = dict_path["history"]
        self.path_to_common_files = dict_path["common"]
        path_lang = dict_path["language"]

        try:
            with open(self.path_to_config, mode="r", encoding="utf-8") as __file:
                __data = json.load(__file)
            
            self.path_to_language = f"{path_lang}/{__data['language']}"
        
        except:
            self.path_to_language = f"C:/Users/salim/AppData/Roaming/PasswordAnalyzer/language/ru-RU.json"

        return
    
    def get_config(self, arg: str | None = None) -> str | int | None:
        if arg is None:
            return None
        
        try:
            with open(self.path_to_config, mode="r", encoding="utf-8") as __file:
                __data = json.load(__file)
        except:
            return None
        
        if not arg in __data.keys():
            return False
        
        return __data[arg]
    
    def get_history(self, amount_history: int = 5) -> list:

        result = list()
        
        try:
            with open(self.path_to_history, mode="r", encoding="utf-8") as __file:
                __data = __file.read()
        except:
            return None

        amount = 1

        for lines in __data.split("\n"):
            if amount > amount_history:
                break
            
            result.append(lines)
            amount += 1
        
        return result

    def add_history(self, message: str | None) -> bool:
        if message is None:
            return False
        

        try:
            with open(self.path_to_history, mode="r", encoding="utf-8") as __file:
                __data = __file.read()
        except:
            return False
        

        text = f"{message}\n{__data}"
        
        try:
            with open(self.path_to_history, mode="w", encoding="utf-8") as __file:
                __file.write(text)

            return True
        except:
            return False
        
    def edit_config(self, name: str | None = None, arg: str | None = None) -> bool:
        if name is None or arg is None:
            return False
        
        try:
            with open(self.path_to_config, mode="r", encoding="utf-8") as __file:
                data = json.load(__file)
        except:
            return False
        
        if not name in data.keys():
            return False
        
        data[name] = arg

        try:
            with open(self.path_to_config, mode="w", encoding="utf-8") as __file:
                json.dump(data, __file, indent=4, ensure_ascii=False)

            return True
        except:
            return False
    
    
    def get_lang(self):
        pass


    def get_common_file(self, level: int | None = None) -> list:
        result = list()

        dict_level = {
            1: "1.txt",
            2: "2.txt",
            3: "3.txt"
        }

        if level is None or not level in dict_level.keys(): return result

        name = dict_level[level]

        path = f"{self.path_to_common_files}/{name}"

        try:
            with open(path, mode="r", encoding="utf-8") as __file:
                __data = __file.read()
            
        except: return result

        result = __data.split("\n")

        result.pop(-1)
        
        return result