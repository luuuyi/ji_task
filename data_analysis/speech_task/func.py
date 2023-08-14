import soundfile as sf
from pydub import AudioSegment
from pydub.silence import split_on_silence
import numpy as np
from noisereduce import reduce_noise

# def denoise(wav_file, output_file):
#     # https://blog.csdn.net/lvsetongdao123/article/details/131468259
#     audio_file, sr = librosa.load(wav_file, sr=None)

#     # 计算噪声阈值
#     threshold_h = librosa.amplitude_to_db(librosa.feature.rms(audio_file), ref=np.max)

#     # 应用噪声过滤器
#     audio_file_denoised = librosa.effects.decompose(audio_file, noise_kernels=[None]*len(audio_file), threshold=threshold_h)

#     # 保存降噪后的音频文件
#     sf.write(output_file, audio_file_denoised, sr)

def denoise(wave_data):
    # https://blog.csdn.net/m0_65478862/article/details/129026317

    # Convert the audio to a numpy array
    audio_array = wave_data.get_array_of_samples()

    # Perform noise reduction on the audio array
    reduced_noise = reduce_noise(audio_array, wave_data.frame_rate)

    # Create a new AudioSegment from the reduced noise array
    reduced_audio = AudioSegment(
        reduced_noise.tobytes(),
        frame_rate=wave_data.frame_rate,
        sample_width=wave_data.sample_width,
        channels=wave_data.channels
    )

    return reduced_audio

def remove_silence(wave_data):
    # https://www.yii666.com/blog/392345.html
    sound = wave_data     
    chunks = split_on_silence(sound,
        # must be silent for at least half a second,沉默半秒
        min_silence_len=600,     
        # consider it silent if quieter than -16 dBFS        
        silence_thresh=-60,
        keep_silence=400     
    )
    sum=sound[:1]    
    for i, chunk in enumerate(chunks):        
        sum=sum+chunk        
    return sum

def increase_sound(wave_data, inc=10):
    # https://www.jb51.net/article/278581.htm
    audio = wave_data
    m_audio = audio + inc
    return m_audio

if __name__ == "__main__":
    wave_data = AudioSegment.from_file("tos.wav")
    # import ipdb; ipdb.set_trace()

    # No.1
    # wave_data = denoise(wave_data)
    # wave_data.export("result.wav", format="wav")

    # wave_data = remove_silence(wave_data)
    # wave_data.export("result.wav", format="wav")

    wave_data = increase_sound(wave_data)
    wave_data.export("result.wav", format="wav")