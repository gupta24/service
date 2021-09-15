from .hmac_signature import hash_function
from fastapi.encoders import jsonable_encoder
import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


secrat_key = b'(1O\x0b+0\xdd\xca8\x11\x9a\xcd\xe6\xd09c'


def check_signature(client_signature, data_message):
    # get the raw data and HMAC signature from client side..
    server_hmac_signature = hash_function(secrat_key, data_message)
    if(server_hmac_signature == client_signature):
        return True
    else:
        return False
