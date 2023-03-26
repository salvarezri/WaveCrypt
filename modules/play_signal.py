# Este modulo tiene como proposito
# recibir un texto para su conversion
# a señal de audio y posterior
# reproduccion.

from .create_signal import generate_array_samples
from .create_signal import fs
from pydub import AudioSegment
from pydub.playback import play


def play_sound(text):

    signal = generate_array_samples(text)
    output_bytes = signal.tobytes()

    audio_segment = AudioSegment(
        output_bytes,
        frame_rate=fs,
        sample_width=signal.dtype.itemsize,
        channels=1
    )

    play(audio_segment)
