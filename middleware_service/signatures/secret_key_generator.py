import secrets

def generate_secrete_key():
    secret_key = secrets.token_bytes(16)
    #print(secret_key)
    return secret_key


secret_key = ''
def set_secret_key(key = b'(1O\x0b+0\xdd\xca8\x11\x9a\xcd\xe6\xd09c'):
    global secret_key
    secret_key = key
    
    
def get_secret_key():
    return secret_key

