import re
import math

class Check:

    level: int

    def __init__(self, level: int = 1) -> None:
        return
    
    def first_check(self, password: str | None = None) -> dict:
        result = dict()
        
        if password is None: return result
        

        score = 0

        message = dict()
        list_name = ["len-8", "A-Z", "a-z", "!@$", "0-9", "entropy"]

        for name in list_name: message[name] = False

        if len(password) >= 8:
            score += 15
            message["len-8"] = True

            if len(password) >= 16:
                score += 15
            
        else:
            score += -5



        if bool(re.search(pattern=r"[A-Z]", string=password)) or bool(re.search(pattern=r"[А-Я]", string=password)):
            message["A-Z"] = True
            score += 10

        else:
            score += -5
        


        if bool(re.search(pattern=r"[a-z]", string=password)) or bool(re.search(pattern=r"[а-я]", string=password)):
            message["a-z"] = True
            score += 10

        else:
            score += -5



        if bool(re.search(pattern=r"[!\"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", string=password)):
            message["!@$"] = True
            score += 15

        else:
            score += -5


        if bool(re.search(pattern=r"\d", string=password)):
            message["0-9"] = True
            score += 10

        else:
            score += -5

        entropy = self.entropy_check(password=password)

        entropy_list = {"numbers": entropy,
                        "result": False} # [numbers, result]

        if entropy < 65.1:
            entropy_list["result"] = False
            score += -10
        else:
            entropy_list["result"] = True
            score += 15

        message["entropy"] = entropy_list



        result["score"] = score # max -- 90
        result["message"] = message

        return result
    
    
    def second_check(self, password: str | None = None, common_file: list | None = None) -> dict:
        result = dict()

        if password is None or common_file is None: return result

        score = 0
        message = dict()

        message["clear"] = True
        message["1in1"] = False
        message["like"] = ""

        for name in common_file:
            if name.lower() == password.lower():
                score += -25
                message["clear"] = False
                message["1in1"] = True
                break

        if message["clear"]:
            for name in common_file:
                if password.lower() in name.lower() and len(password) <= (len(name)+4):
                    score += -10
                    message["clear"] = False
                    message["like"] = name
                    break

        if score > -1:
            score += 10

        result["score"] = score
        result["message"] = message

        return result
    
    def entropy_check(self, password: str | None = None) -> float:
        if password is None: return -1

        number_bits = 0

        alphabet = 0

        alphabet_dictionaries = {
            r"[A-Z]": 26,
            r"[a-z]": 26,
            r"[А-Я]": 33,
            r"[а-я]": 33,
            r"[!\"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]": 40,
            r"\d": 10
        }

        for i in alphabet_dictionaries.keys():
            if bool(re.search(i, password)):
                alphabet += int(alphabet_dictionaries[str(i)])

        if alphabet <= 0: alphabet = 1


        number_bits = len(password) * math.log2(alphabet)

        return round(number_bits, 2)