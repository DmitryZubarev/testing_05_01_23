from pydantic import BaseModel, validator
import re


"""This class will be used to validate incoming json files on post request with path '/check ' """
class User(BaseModel):
    email: str
    login: str
    phone: str

    # validation of email
    @validator('email')
    def check_email(cls, v):
        result = re.split("@", v)
        if (not len(result) == 2) or result[0][0] == '.':
            raise ValueError('Email must be must be in the form user@domain')
        if result[0] == '' or result[1] == '':
            raise ValueError('Email must be must be in the form user@domain')
        return v

    # validation of login
    @validator('login')
    def check_login(cls, v):
        if 3 <= len(v) <= 20:
            for char in v:
                if not (97 <= ord(char) <= 122 or 48 <= ord(char) <= 57 or ord(char) == 46):
                    raise ValueError('The login must include only the characters a-z 0-9 and .')
        else:
            raise ValueError('The login must include only the characters a-z 0-9 and .')
        return v

    # validation of phone number
    @validator('phone')
    def check_phone(cls, v):
        if len(v) == 12 and v[0:3] == "+79":
            for char in v[3:]:
                if not (48 <= ord(char) <= 57):
                    raise ValueError('Phone should be in the form +79XXXXXXXXX')
        else:
            raise ValueError('Phone should be in the form +79XXXXXXXXX')
        return v
