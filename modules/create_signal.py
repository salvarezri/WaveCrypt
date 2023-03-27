# Este modulo tiene como proposito
# recibir un texto y convertirlo a
# un arreglo de frecuencias mapeadas
# a cada uno de los caracteres del
# arreglo.

import numpy as np

# ascii no extendido, caracteres imprimibles
min_char_ascii = 32
max_char_ascii = 126

# Debemos crear el arreglo con los valores
# de la onda a reproducir, estos se obtienen
# del texto encriptado y se mappean usando
# el codigo ascii y el rango de las
# frecuencias determinado. Para esto debemos
# normalizar el codigo ascii de cada caracter
# de la cadena.

# nos aseguramos de que cada una de los caracteres
# tenga una frecuencia como imagen o absisa.
# rango de freq. usadas: [300, step_freq*(max_char_ascii-min_char_ascii)]
step_freq = 20
initial_freq_hz = 20

# tiempo de reproduccion por caracter (en segundos)
play_t = 0.05

# frecuencia de muestreo (en Hz), debe ser entero
fs = 48000


def generate_array_samples(text):
    # text: texto o cadena a mappear

    text_size = len(text)
    new_arr = np.zeros(1)

    for i in range(text_size):
        char_freq = (ord(text[i]) - min_char_ascii) * step_freq + initial_freq_hz
        arr = np.arange(fs * play_t) * char_freq
        new_arr = np.concatenate((new_arr, arr), axis=None)

    # generacion de la muestra, el tipo del array de deja en float32 (-1.0, 1.0)
    sample = (np.sin(2 * np.pi * new_arr / fs)).astype(np.float32)
    # print(len(sample))
    return sample
