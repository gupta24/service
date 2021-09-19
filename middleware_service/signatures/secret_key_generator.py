default_secret_key = b'(1O\x0b+0\xdd\xca8\x11\x9a\xcd\xe6\xd09c'
input_secret_key = ''
is_setup_key = False


def generate_secret_key(input_byte_key):
    global input_secret_key
    global is_setup_key
    input_secret_key = input_byte_key
    is_setup_key = True
    print(is_setup_key)

    
def get_secret_key():
    global is_setup_key
    global default_secret_key
    global input_secret_key
    if is_setup_key:
        is_setup_key = False
        print(is_setup_key)
        return input_secret_key
    return default_secret_key

