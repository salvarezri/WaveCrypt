# - Interfaz / Santiago
# - Lectura de txt / Santiago
# - Codificación - Decodificación / Santiago

# - Creación de señal / yoxd
# -* reproducir la señal de audio / yo xd

from random import randrange

import numpy as np
from pydub import AudioSegment
from pydub.playback import play


def funcion():
    """
     Esta es la cadena de texto recibida (cifrada) que se debe
     mappear a numeros dentro de un rango (300 hz y x hz) de
     sonido audible para su posterior reproduccion.

    """
    # text_encrypted = "cadena-ejemplo:la@skdjflk298fe-"

    # ascii no extendido, caracteres imprimibles
    min_char_ascii = 32
    max_char_ascii = 126

    # nos aseguramos de que cada una de los caracteres
    # tenga una frecuencia como imagen o absisa.
    # rango de freq. usadas: (300, 10000)
    step_freq = 20
    initial_freq_hz = 300

    # tiempo de reproduccion por caracter (en segundos)
    play_t = 0.2

    # vars de pruebas
    string_size = 10

    def create_rand_ascii(size):
        new_string = ''
        for i in range(size):
            new_string += chr(randrange(min_char_ascii, max_char_ascii))
        return new_string

    text_encrypted = create_rand_ascii(string_size)

    # vars de pruebas

    # Debemos crear el arreglo con los valores
    # de la onda a reproducir, estos se obtienen
    # del texto encriptado y se mappean usando
    # el codigo ascii y el rango de las
    # frecuencias determinado. Para esto debemos
    # normalizar el codigo ascii de cada caracter
    # de la cadena.

    fs = 48000  # sampling rate, Hz, must be integer
    # duration = 4.0  # in seconds, may be float
    # f = 400.0  # sine frequency, Hz, may be float
    # generate samples, note conversion to float32 array
    # samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

    def generate_array_samples(text):
        text_size = len(text)
        new_arr = np.zeros(1)

        for i in range(text_size):
            char_freq = (ord(text[i]) - min_char_ascii) * step_freq + initial_freq_hz
            arr = np.arange(fs * play_t) * char_freq
            new_arr = np.concatenate((new_arr, arr), axis=None)

        return (np.sin(2 * np.pi * new_arr / fs)).astype(np.float32)

    # text_encrypted = ''
    signal = generate_array_samples(text_encrypted)
    output_bytes = signal.tobytes()

    audio_segment = AudioSegment(
        output_bytes,
        frame_rate=fs,
        sample_width=signal.dtype.itemsize,
        channels=1
    )

    play(audio_segment)

    """
    # escribir el arreglo
    f = open("demofile2.txt", "a")
    for i in range(len(samples)):
        f.write('\n'+str(samples[i]))

    f.close()
    """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    funcion()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Mayús+F10 to execute it or replace it with your code.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
