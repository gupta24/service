from .hmac_signature import hash_function
from .secret_key_generator import set_secret_key ,get_secret_key
from fastapi.encoders import jsonable_encoder
import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

set_secret_key()
secrat_key = get_secret_key()
logger.info(secrat_key)

def check_signature(client_signature, data_message):
    # get the raw data and HMAC signature from client side..
    server_hmac_signature = hash_function(secrat_key, data_message)
    if(server_hmac_signature == client_signature):
        return True
    else:
        return False
