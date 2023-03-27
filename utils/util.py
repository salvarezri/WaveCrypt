from random import randrange

from modules.play_signal import play_sound


# funcion para generar cadenas aleatorias
def create_rand_ascii(size):
    new_string = ''
    for i in range(size):
        new_string += chr(randrange(32, 126))
    return new_string


def play():
    # texto recibido a reproducir
    string_size = 20
    example_text_encrypted = '---- LIMITE TRAMA ----' + create_rand_ascii(string_size) + '---- LIMITE TRAMA ----'

    # (escribir entre LIMITE TRAMA)
    # example_text_encrypted = '---- LIMITE TRAMA ----' \
                             # 'este es un ejemplo "real?"' \
                             # '---- LIMITE TRAMA ----'

    # esta funcion puede ser activada (antes importada) por la interfaz
    play_sound(example_text_encrypted)
