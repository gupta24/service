import os
from dotenv import load_dotenv, find_dotenv


default_secret_key = b'(1O\x0b+0\xdd\xca8\x11\x9a\xcd\xe6\xd09c'
load_dotenv(find_dotenv())


def KeyError(BaseException):
    pass


def get_secret_key():
    global default_secret_key

    try:
        print(find_dotenv())
        secret_key = os.environ['SECRET_KEY']
        print(secret_key)
        secret_key = secret_key.encode('ascii')
    except BaseException as e:
        raise KeyError("SECRET_KEY does not exist in .env file, setup variable name in your .env")

    print(secret_key)
    return secret_key

