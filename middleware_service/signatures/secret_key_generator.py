import os
from dotenv import load_dotenv, find_dotenv

path = find_dotenv()
load_dotenv(path)

def KeyError(BaseException):
    pass


def get_secret_key():
    try:
        secret_key = os.environ['SECRET_KEY']
        print(secret_key)
        secret_key = secret_key.encode('ascii')
    except BaseException as e:
        raise KeyError("SECRET_KEY does not exist in .env file, setup variable name in your .env")

    print(secret_key)
    return secret_key

