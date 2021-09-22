import os
import sys
from dotenv import load_dotenv, find_dotenv

#path = find_dotenv('.env',False, False)
filename = '.env'
frame = sys._getframe()
# find first frame that is outside of this file
while frame.f_code.co_filename == __file__:
    frame = frame.f_back
frame_filename = frame.f_code.co_filename
path = os.path.dirname(os.path.abspath(frame_filename))
load_dotenv(path)

#def KeyError(BaseException):
#    pass


def get_secret_key():
#    try:
    print(path)
    secret_key = os.getenv('SECRET_KEY')
    print(secret_key)
    #secret_key = secret_key.encode('ascii')
#    except BaseException as e:
#        raise KeyError("SECRET_KEY does not exist in .env file, setup variable name in your .env")

    print(secret_key)
    return b'(1O\x0b+0\xdd\xca8\x11\x9a\xcd\xe6\xd09c'

