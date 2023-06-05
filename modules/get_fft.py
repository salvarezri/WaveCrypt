import numpy as np
from scipy.fft import fft, fftshift


def return_freq_array(start, end, array, fs):
    arr_fft = fft(array[start:end])
    arr_fft = abs(arr_fft) * 2.0 / fs
    arr_fft = fftshift(arr_fft)

    arr_size = end - start + 1

    arr_fft = arr_fft[int(arr_size / 2):arr_size]
    freq_array = np.arange(0, (arr_size / 2) - 1) / arr_size

    ind = np.argmax(arr_fft)
    freq = freq_array[ind]

    return fs * freq
