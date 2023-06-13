from modules.get_fft import return_freq_array
from pydub import AudioSegment


def refine_interval(freq, start, end, array, fs):
    num_interval = 4
    interval_length = int((end - start) / num_interval)

    low_interval = 0
    prev_interval_freq = return_freq_array(start + interval_length * low_interval,
                                           start + interval_length * (low_interval + 1), array, fs)
    last_interval_freq = return_freq_array(start + interval_length * (low_interval + 1),
                                           start + interval_length * (low_interval + 2), array, fs)

    valid_change = (round(last_interval_freq) != round(prev_interval_freq)) & (
                (round(freq) == round(last_interval_freq)) | (round(freq) == round(prev_interval_freq)))
    while not valid_change and low_interval < num_interval - 2:
        low_interval += 1
        prev_interval_freq = last_interval_freq
        last_interval_freq = return_freq_array(start + interval_length * (low_interval + 1),
                                               start + interval_length * (low_interval + 2), array, fs)

        valid_change = (round(last_interval_freq) != round(prev_interval_freq)) & (
                (round(freq) == round(last_interval_freq)) | (round(freq) == round(prev_interval_freq)))

    interval_change = low_interval + 1

    in_prev_interval = round(prev_interval_freq) == round(freq)
    in_last_interval = round(last_interval_freq) == round(freq)
    if in_prev_interval and not in_last_interval:
        return start + (num_interval - interval_change) * interval_length
    elif in_last_interval and not in_prev_interval:
        return start + interval_change * interval_length
    return start


def recover_string_from_signal(filename = ""):

    # esto usa un audio ejemplo, se supone que el param. signal es la señal del audio
    sound = AudioSegment.from_wav(file=filename) ## tambien puede usarse .from_wav()
    sound = sound.set_channels(1)
    arr1 = sound.get_array_of_samples()
    # se reemplaza en el codigo arr1 por signal, o se puede pasar un audio y se reemplaza sound por signal

    initial_freq = 20  # 280
    step_freq = 20
    min_char_ascii = 32

    limit_freq = 280

    time_per_char = 0.05
    limit_sample_size = int(sound.frame_rate * 4 * time_per_char)

    max_intervals = int(len(arr1) / limit_sample_size) - 1
    great_interval = 0
    freq = return_freq_array(limit_sample_size * great_interval, limit_sample_size * (great_interval + 1), arr1, sound.frame_rate)
    while (round(freq) != limit_freq) & (great_interval < max_intervals):
        great_interval += 1
        freq = return_freq_array(limit_sample_size * great_interval, limit_sample_size * (great_interval + 1), arr1, sound.frame_rate)

    real_start_limit = refine_interval(freq, limit_sample_size * great_interval, limit_sample_size * (great_interval + 1), arr1, sound.frame_rate)

    #print("Intervalo #", great_interval)
    #print("Inicio index #", great_interval * limit_sample_size)
    #print(freq)
    #print("Inicio real: ", real_start_limit)

    recovered_string = ""
    limit_reached = 0
    char_index = 0
    try :
        while limit_reached < 3 and char_index < 20:
            char_freq = return_freq_array(real_start_limit + 52800 + (char_index * 2400),
                                          real_start_limit + 52800 + ((char_index + 1) * 2400), arr1, sound.frame_rate)
            ord_char = round((char_freq - initial_freq) / step_freq) + min_char_ascii

            if round(char_freq) == limit_freq:
                limit_reached += 1
            else:
                recovered_string += chr(ord_char)

            #print("Letra: ", chr(ord_char), " / ASCII: ", ord_char)

            char_index += 1

        return recovered_string
    except:
        print()
        return 0


if __name__ == '__main__':# BORRAR
    print(recover_string_from_signal("../records/2023-06-10 18:45:58.005115.wav"))
