import secrets

secret_key = b'(1O\x0b+0\xdd\xca8\x11\x9a\xcd\xe6\xd09c'
def generate_secrete_key():
    global secret_key
    secret_key = secrets.token_bytes(16)
    #print(secret_key)
    
def get_secret_key():
    return secret_key

