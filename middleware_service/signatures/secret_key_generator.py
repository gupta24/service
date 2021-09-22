import os
import sys
from dotenv import load_dotenv
from typing import (IO, Dict, Iterable, Iterator, Mapping, Optional, Tuple, Union)



def _walk_to_root(path: str) -> Iterator[str]:
    """
    Yield directories starting from the given directory up to the root
    """
    if not os.path.exists(path):
        raise IOError('Starting path not found')

    if os.path.isfile(path):
        path = os.path.dirname(path)

    last_dir = None
    current_dir = os.path.abspath(path)
    while last_dir != current_dir:
        yield current_dir
        parent_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
        last_dir, current_dir = current_dir, parent_dir


def find_env():
    filename = '.env'
    frame = sys._getframe()
    # find first frame that is outside of this file
    while frame.f_code.co_filename == __file__:
        frame = frame.f_back
    frame_filename = frame.f_code.co_filename
    path = os.path.dirname(os.path.abspath(frame_filename))

    for dirname in _walk_to_root(path):
        check_path = os.path.join(dirname, filename)
        if os.path.isfile(check_path):
            return check_path
    
    return ''
    
#filepath = os.path.join(dirname, filename)
filepath = find_env()
load_dotenv(filepath)


def KeyError(BaseException):
    pass


def get_secret_key():
    try:
        print(filepath)
        secret_key = os.getenv('SECRET_KEY')
        print(secret_key)
        secret_key = secret_key.encode('ascii')
    except BaseException as e:
        raise KeyError("SECRET_KEY does not exist in .env file, setup variable name in your .env")

    print(secret_key)
    return secret_key

