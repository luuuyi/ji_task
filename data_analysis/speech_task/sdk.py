from pydub import AudioSegment

import speech_task.func as speech_task_func

def call_speech_task(input_path, output_path, args):
    try:
        wave_data = AudioSegment.from_file(input_path)

        # No.1
        if args["denoise_flag"]:
            wave_data = speech_task_func.denoise(wave_data)

        # No.2
        if args["remove_silence_flag"]:
            wave_data = speech_task_func.remove_silence(wave_data)

        # No.3
        inc = args["increase_sound_args"]["inc"]
        if args["increase_sound_flag"]:
            wave_data = speech_task_func.increase_sound(wave_data, inc)

        wave_data.export(output_path)
        message = "success"
        code    = 1
    except Exception as e:
        code    = 3
        message = f"{e}"
    return code, message