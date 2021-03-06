from .hmac_signature import hash_function
from .secret_key_generator import get_secret_key
import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


secrat_key = get_secret_key()

def check_signature(client_signature, data_message):
    # get the raw data and HMAC signature from client side..
    print(secrat_key)
    print(type(secrat_key))
    server_hmac_signature = hash_function(secrat_key, data_message)
    print(server_hmac_signature)
    if(server_hmac_signature == client_signature):
        return True
    else:
        return False
