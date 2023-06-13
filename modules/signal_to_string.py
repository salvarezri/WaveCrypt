from modules.get_fft import return_freq_array
from pydub import AudioSegment

initial_freq = 280
step_freq = 20
min_char_ascii = 32

limit_freq = 3080
limit_freq_char = ((limit_freq - initial_freq) / 20) + min_char_ascii


def refine_interval(start, end, array, fs):
    num_interval = 4
    interval_length = int((end - start) / num_interval)

    low_interval = 0
    prev_interval_freq = return_freq_array(start + interval_length * low_interval,
                                           start + interval_length * (low_interval + 1), array, fs)
    last_interval_freq = return_freq_array(start + interval_length * (low_interval + 1),
                                           start + interval_length * (low_interval + 2), array, fs)

    valid_change = (round(((last_interval_freq - initial_freq) / 20) + min_char_ascii) != round(
        ((prev_interval_freq - initial_freq) / 20) + min_char_ascii)) & (
                           (limit_freq_char == round(last_interval_freq)) | (
                               limit_freq_char == round(prev_interval_freq)))

    while not valid_change and low_interval < num_interval - 2:
        low_interval += 1
        prev_interval_freq = last_interval_freq
        last_interval_freq = return_freq_array(start + interval_length * (low_interval + 1),
                                               start + interval_length * (low_interval + 2), array, fs)

        valid_change = (round(((prev_interval_freq - initial_freq) / 20) + min_char_ascii) != round(
            ((last_interval_freq - initial_freq) / 20) + min_char_ascii)) & (
                               (limit_freq_char == round(
                                   ((last_interval_freq - initial_freq) / 20) + min_char_ascii)) | (
                                           limit_freq_char == round(
                                       ((prev_interval_freq - initial_freq) / 20) + min_char_ascii)))

    interval_change = low_interval + 1

    in_prev_interval = round(((prev_interval_freq - initial_freq) / 20) + min_char_ascii) == limit_freq_char
    in_last_interval = round(((last_interval_freq - initial_freq) / 20) + min_char_ascii) == limit_freq_char
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

    time_per_char = 0.05
    limit_sample_size = int(sound.frame_rate * 4 * time_per_char)

    max_intervals = int(len(arr1) / limit_sample_size) - 1
    great_interval = 0
    freq = return_freq_array(limit_sample_size * great_interval, limit_sample_size * (great_interval + 1), arr1, sound.frame_rate)
    while (round(((freq - initial_freq) / 20) + min_char_ascii) != limit_freq_char) & (great_interval < max_intervals):
        great_interval += 1
        freq = return_freq_array(limit_sample_size * great_interval, limit_sample_size * (great_interval + 1), arr1, sound.frame_rate)
        #print("int: ", great_interval, round(freq), limit_freq)

    real_start_limit = refine_interval(limit_sample_size * great_interval, limit_sample_size * (great_interval + 1), arr1, sound.frame_rate)

    #print("Intervalo #", great_interval)
    #print("Inicio index #", great_interval * limit_sample_size)
    #print(freq)
    #print("Inicio real: ", real_start_limit)

    recovered_string = ""
    limit_reached = 0
    char_index = 0
    try :
        while limit_reached < 4 and char_index < (max_intervals + 1) * limit_sample_size / 2400:
            char_freq = return_freq_array(real_start_limit + 12000 + (char_index * 2400),
                                          real_start_limit + 12000 + ((char_index + 1) * 2400), arr1, sound.frame_rate)
            ord_char = round((char_freq - initial_freq) / step_freq) + min_char_ascii

            if ord_char == limit_freq_char:
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
