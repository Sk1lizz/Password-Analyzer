import random

"""

"""


class generate_password:
    length: int #
    upper: bool # 
    lower: bool # 
    special_char: bool # 
    numbers: bool #
    russian_letters : bool #

    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    UPPER_RUSSIAN = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    LOWER = "abcdefghlijkmnopqrstuvwxyz"
    LOWER_RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    SPECIAL_CHAR = r"[!\"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]"
    NUMBERS = "0123456789"

    confirm_setting: bool # 

    def __init__(self) -> None:
        self.confirm_setting = False
        return
    
    
    def generate_password(self) -> str:
        if not self.confirm_setting: return "Not confirm setting"

        password = ""

        while len(password) <= self.length:
            
            if self.upper:
                if self.russian_letters:
                    i = random.randint(0, (len(self.UPPER_RUSSIAN) - 1 ))
                    password += self.UPPER_RUSSIAN[i]

                else:
                    i = random.randint(0, (len(self.UPPER) - 1 ))
                    password += self.UPPER[i]

            if self.lower:
                if self.russian_letters:
                    i = random.randint(0, (len(self.LOWER_RUSSIAN) - 1 ))
                    password += self.LOWER_RUSSIAN[i]

                else:
                    i = random.randint(0, (len(self.LOWER) - 1 ))
                    password += self.LOWER[i]

            if self.special_char and ((len(password) % 5 == 0) or (len(password) % 5 == 2) or (len(password) % 5 == 3)) and len(password) > 4:
                i = random.randint(0, (len(self.SPECIAL_CHAR) - 1 ))
                password += self.SPECIAL_CHAR[i]

            if self.numbers and len(password) >= (self.length // 2):
                i = random.randint(0, (len(self.NUMBERS) - 1 ))
                password += self.NUMBERS[i]

        return password
    
    
    def set_setting(self, length: int = 16, upper_bool: bool = True, lower_bool: bool = True, special_chars_bool: bool = True, numbers_bool: bool = True, russian_letters: bool = False) -> bool:
        self.length = length
        self.upper = upper_bool
        self.lower = lower_bool
        self.special_char = special_chars_bool
        self.numbers = numbers_bool
        self.russian_letters = russian_letters

        self.confirm_setting = True

        return True