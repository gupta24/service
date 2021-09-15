import secrets

def generate_secrete_key():
    secret_key = secrets.token_bytes(16)
    #print(secret_key)
    return secret_key
