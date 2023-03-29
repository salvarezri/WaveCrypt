from Crypto.Cipher import Salsa20


def validate_password(text=""):
    # password must be alphanumeric and has between 8 and 16 character size
    if (not text.isalnum())\
            or len(text) < 8 \
            or len(text) > 16:
        return False
    return True


def validate_text(text=""):
    # text must be in ascii
    if not text.isascii():
        return False
    return True


def transform_password(password=""):
    # transform the password to an acceptable password
    pass_len = len(password)
    max_len = 16
    new_pass = password
    for i in range(pass_len, max_len):
        new_pass += "Z"
    return new_pass


def encrypt(text="", password=""):
    # transform password and text into bytes
    plaintext = text.encode()
    secret = transform_password(password).encode()
    # print(len(secret))
    # get the encrypted text
    cipher = Salsa20.new(key=secret)
    msg = cipher.nonce + cipher.encrypt(plaintext)
    # when is encrypted, it returns byte object, so we pass it to str
    msg2 = str(msg)
    return msg2


def decrypt(text="", password=""):
    # get password
    secret = transform_password(password).encode('ascii')
    # we use eval to transform the str to bytes
    msg = eval(text)
    # divide the nonce from the text
    msg_nonce = msg[:8]
    ciphertext = msg[8:]
    # get the decrypted byte
    cipher = Salsa20.new(key=secret, nonce=msg_nonce)
    plaintext = cipher.decrypt(ciphertext)
    # pass to string
    return str(plaintext)[2:-1]
