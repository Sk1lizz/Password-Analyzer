import re

"""

"""

class Check:

    level: int

    def __init__(self, level: int = 1) -> None:
        return
    
    def first_check(self, password: str | None = None) -> dict:
        result = dict()
        
        if password is None: return result
        

        score = 0

        message = dict()
        list_name = ["len-8", "len-16", "A-Z", "a-z", "!@$", "0-9"]

        for name in list_name: message[name] = False

        if len(password) >= 8:
            score += 15
            message["len-8"] = True

            if len(password) >= 16:
                score += 15
                message["len-16"] = True
            
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


        result["score"] = score
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
                if password.lower() in name.lower() and len(password) >= (len(name)+4):
                    score += -10
                    message["clear"] = False
                    message["like"] = name

        if score > -1:
            score += 10

        result["score"] = score
        result["message"] = message

        return result