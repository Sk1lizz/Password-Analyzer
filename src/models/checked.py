import re

"""

"""

class Check:

    def __init__(self) -> None:
        return
    
    def first_check(self, password: str | None = None) -> dict:
        result = dict()
        
        if password is None:
            return result
        
        

        """
        ----- dict model -----
        
    {
        "score": int,
        "message": {
            name: bool
        }

    }

        """

        score = 0

        message = dict()
        list_name = ["len-8", "len-16", "A-Z", "a-z", "!@$", "0-9"]

        for i in list_name:
            message[i] = False

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
