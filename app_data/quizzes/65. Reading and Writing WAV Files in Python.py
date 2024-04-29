# # 1==========================================================================


# ? Why is the WAV file format still widely used despite its age?


# - It’s the only format supported by all operating systems.
# - It’s the only format that can store raw, uncompressed audio data.
# - It’s the smallest audio file format.
# + It’s simple, portable, and provides high-fidelity sound.


# ! The <a
# / href="https://realpython.com/python-wav-files/#understand-the-wav-file-format"
# / target="_blank">WAV file format</a>
# ! is still widely used because of its simplicity, portability, and
# / high-fidelity sound.


# * The WAV file format has some key advantages that have helped it stand the
# / test of time.


# > https://realpython.com/quizzes/python-wav-files/


# # 2==========================================================================


# ? What does the vertical axis represent in an audio waveform?


# + The amplitude at any given point in time
# - The frequency of the sound
# - The duration of the audio track
# - The phase of the sound wave


# ! In an audio waveform, the vertical axis represents the amplitude at any
# / given point in time.
# ! The midpoint of the graph, which is a horizontal line passing through the
# / center, represents the baseline amplitude or the point of silence.
# ! Any deviation from this equilibrium corresponds to a higher positive or
# / negative amplitude, which you experience as a louder sound.
# ! You can learn more about this in the section on <a
# / href="https://realpython.com/python-wav-files/#the-waveform-part-of-wav"
# / target="_blank">the waveform part of WAV</a>.


# * Think about what changes as you move up and down on the graph.


# > https://realpython.com/quizzes/python-wav-files/


# # 3==========================================================================


# ? What are the key parameters found in a WAV file header?
# ? (Select all that apply.)


# + Bit Depth
# + Encoding
# + Frame Rate
# + Channel Count
# - Creation Date
# - File Size


# ! A WAV file begins with a header comprising metadata, which describes how
# / to interpret the sequence of audio frames that follow. The most important
# / parameters that you’ll find in a WAV header are:


# * The WAV file header contains metadata that describes how to interpret the
# / sequence of audio frames that follow.


# > https://realpython.com/quizzes/python-wav-files/


# # 4==========================================================================


# ? What are the four integer-based, uncompressed PCM encoding bit depths that
# / Python’s wave module supports?


# - 8-bit signed integer, 16-bit unsigned integer, 24-bit signed integer, 32-bit signed integer
# - 8-bit signed integer, 16-bit signed integer, 24-bit unsigned integer, 32-bit signed integer
# + 8-bit unsigned integer, 16-bit signed integer, 24-bit signed integer, 32-bit signed integer
# - 8-bit signed integer, 16-bit signed integer, 24-bit signed integer, 32-bit unsigned integer


# ! Python’s wave module supports four integer-based, uncompressed PCM
# / encoding bit depths:


# * Think about which bit depth needs special treatment.


# > https://realpython.com/quizzes/python-wav-files/


# # 5==========================================================================


# ? You’ve learned how to read WAV files in Python. What are the steps to do
# / this?
# ? (Select all that apply.)


# + Call wave.open() with the path to your WAV file
# + Import the wave module
# - Call wave.read() with the path to your WAV file
# + Call .readframes() on the Wave_read instance to get the audio frames
# + Call .getparams() on the Wave_read instance to get the file’s metadata
# - Call .getframes() on the Wave_read instance to get the audio frames


# ! To read a WAV file in Python, you need to follow these steps:


# * Remember, the <code>wave</code> module provides a function to open WAV
# / files, and <code>Wave_read</code> instances have methods to get the file’s
# / metadata and audio frames.


# > https://realpython.com/quizzes/python-wav-files/


# # 6==========================================================================


# ? Fill in the blanks:
# ? In Python, you can create a sound wave by using the math module and the
# / wave module.
# ? Here’s a simplified version of how you can do it: ...

# ? This script creates a sound wave with a frequency of _____ Hz that lasts
# / for 2.5 seconds.
# ?  The sound wave is then saved to a file named output.wav.

import math
import wave


def sound_wave(frequency, num_seconds):
    for frame in range(round(num_seconds * 44100)):
        time = frame / 44100
        amplitude = math.sin(2 * math.pi * frequency * time)
        yield round((amplitude + 1) / 2 * 255)
        with wave.open("output.wav", mode="wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(1)
            wav_file.setframerate(44100)
            wav_file.writeframes(bytes(sound_wave(440, 2.5)))


# + 440
# - 44100

# ! The script creates a sound wave with a frequency of 440 Hz that lasts for
# / 2.5 seconds.
# ! The sound wave is then saved to a file named <code>output.wav</code>.

# > https://realpython.com/quizzes/python-wav-files/


# # 7==========================================================================


# ? How do you create a stereo audio signal in a WAV file?


# - Duplicate the mono audio signal for both channels
# - Subtract the right channel audio samples from the left channel
# + Interleave the audio samples from the left and right channels in each frame
# - Add the audio samples from the left and right channels together


# ! To create a stereo audio signal in a WAV file, you need to interleave the
# / audio samples from the left and right channels in each frame. This can be
# / done using Python’s <code>itertools.chain()</code> function and the
# / <code>zip()</code> function:


# * It’s all about the mix!


# > https://realpython.com/quizzes/python-wav-files/


# # 8==========================================================================


# ? What do integer members of the PCMEncoding enum represent in the context
# / of audio encoding?


# + The number of bytes occupied by a single audio sample in each encoding format
# - The number of bits in each audio sample
# - The range of values supported by an encoding
# - The minimum and maximum values of audio samples


# ! The <code>PCMEncoding</code> class is an enumeration that represents the
# / number of bytes occupied by a single audio sample in each encoding format.
# / For instance, the <code>SIGNED_16</code> member has a value of two because
# / the corresponding 16-bit PCM encoding uses exactly two bytes per audio
# / sample. You can find more details in the section on <a
# / href="https://realpython.com/python-wav-files/#enumerate-the-encoding-formats"
# / target="_blank">enumerating the encoding formats</a>.


# * Think about the header field in the WAV file that they map to.


# > https://realpython.com/quizzes/python-wav-files/


# # 9==========================================================================


# ? How can you decode 24-bit PCM audio samples into amplitudes?
# ? (Select all that apply.)


# - Use an FFT algorithm to convert the bytes into frequency domain before decoding
# + Interpret the bytes as 24-bit integers using the int.from_bytes() function
# + Reshape the array of bytes into a matrix, pad it with zeros, flatten it, and reinterpret the bytes as 32-bit signed integers
# - Interpret the bytes as 8-bit unsigned integers without any conversion


# ! To decode 24-bit audio samples in pure Python, you can iterate over the
# / byte stream in steps of three, corresponding to the three bytes of each
# / audio sample. Then, you can convert such a byte triplet to a Python
# / <code>int</code>, specifying the byte order and the sign bit’s
# / interpretation using <code>int.from_bytes()</code>:


# * Consider the data type sizes and the operations needed to convert a
# / sequence of bytes into a usable audio sample format.


# > https://realpython.com/quizzes/python-wav-files/


# # 10=========================================================================


# ? What does the @cached_property decorator do in the context of the
# / WAVReader class?


# + It ensures that the WAV file is read at most once when the property is first accessed
# - It reshapes the NumPy array into a sequence of frames or channels
# - It closes the WAV file before leaving the current block of code
# - It opens the WAV file for reading in binary mode


# ! The <code>@cached_property</code> decorator is used in the
# / <code>WAVReader</code> class to ensure that the WAV file is read at most
# / once when the property is first accessed. The next time you access the
# / property, you’ll reuse the value remembered in the cache. This is a form
# / of <a href="https://en.wikipedia.org/wiki/Memoization"
# / target="_blank">memoization</a>, which is a common technique for
# / optimizing expensive function calls. You can see an example of this in the
# / section on <a
# / href="https://realpython.com/python-wav-files/#load-all-audio-frames-eagerly"
# / target="_blank">loading all audio frames eagerly</a>.


# * Remember, caching is all about saving time!


# > https://realpython.com/quizzes/python-wav-files/


# # 11=========================================================================


# ? How can you read a specific range of audio frames from a WAV file in
# / Python?


# + By using the .setpos() method on the Wave_read object
# - By using the range() function on the WAV file
# - By using the numpy.linspace() function
# - By using Python’s built-in slice() function directly on the WAV file


# ! You can read a specific range of audio frames from a WAV file in Python by
# / calling the <a
# / href="https://docs.python.org/3/library/wave.html#wave.Wave_read.setpos"
# / target="_blank"><code>.setpos()</code></a> method to skip to the desired
# / starting frame in the WAV file. You can find more details in the section
# / on <a
# / href="https://realpython.com/python-wav-files/#read-a-slice-of-audio-frames"
# / target="_blank">reading a slice of audio frames</a>.


# * You need to convert time to frame indices!


# > https://realpython.com/quizzes/python-wav-files/


# # 12=========================================================================


# ? Why might you want to read a large WAV file in chunks using lazy
# / evaluation?


# - To make the file processing slower
# - To increase the file size
# - To convert the file to a different format
# + To improve memory use efficiency


# ! When dealing with large WAV files, reading the file in chunks using lazy
# / evaluation can
# ! <a
# / href="https://realpython.com/python-wav-files/#process-large-wav-files-in-python-efficiently"
# / target="_blank">improve memory use efficiency</a>.
# ! This is because WAV files typically contain uncompressed data and can
# / reach considerable sizes,
# ! which can make their processing extremely slow or even prevent you from
# / fitting the entire file into memory at once.


# * Think about the challenges of dealing with large files.


# > https://realpython.com/quizzes/python-wav-files/


# # 13=========================================================================


# ? What does the width of each vertical bar in a spectrogram visualization
# / represent?


# - The amplitude of the sound
# - The energy level of the sound
# - The duration of the sound
# + A range of frequencies or a frequency band


# ! In a <a
# / href="https://realpython.com/python-wav-files/#show-a-real-time-spectrogram-visualization"
# / target="_blank">spectrogram visualization</a>,
# ! the width of each vertical bar corresponds to a range of frequencies or a
# / frequency band.
# ! The height of the bar depicts the relative energy level within that band
# / at any given moment.
# ! Frequencies increase from left to right, with lower frequencies
# / represented on the left side of the spectrum
# ! and higher frequencies toward the right.


# * Think about what a spectrogram shows.


# > https://realpython.com/quizzes/python-wav-files/


# # 14=========================================================================


# ? You’re writing a Python script to record an Internet radio stream to a
# / local WAV file. What are the key steps in this process?
# ? (Select all that apply.)


# + Open the radio stream using its URL.
# + Use the obtained metadata for the output WAV file.
# + Loop over the stream and append each decoded chunk of audio channels to the file.
# - Manually set the frame rate, number of channels, and bit depth for the output WAV file.
# - Convert the stream to MP3 format before recording.


# ! To record an Internet radio stream to a local WAV file, you need to:


# * The script should be able to handle the stream’s metadata automatically.
# * There’s no need to convert the stream to another format before recording.


# > https://realpython.com/quizzes/python-wav-files/


# # 15=========================================================================


# ? You’ve learned how to widen the stereo field of a WAV file. What are the
# / steps in this process?
# ? (Select all that apply.)


# + Converting the left and right channels into the mid and side channels
# + Boosting the side channel
# - Boosting the mid channel
# + Converting the mid and side channels back to the left and right channels


# ! To widen the stereo field of a WAV file, you first convert the left and
# / right channels into the mid and side channels.


# * Remember that the side channel captures the differences between the left
# / and right channels.


# > https://realpython.com/quizzes/python-wav-files/
