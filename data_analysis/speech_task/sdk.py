from pydub import AudioSegment

import speech_task.func as speech_task_func

def call_speech_task(input_path, output_path, args):
    try:
        wave_data = AudioSegment.from_file(input_path)

        # No.1
        if args.get("denoise_flag", 0):
            wave_data = speech_task_func.denoise(wave_data)

        # No.2
        if args.get("remove_silence_flag", 0):
            wave_data = speech_task_func.remove_silence(wave_data)

        # No.3
        if args.get("increase_sound_flag", 0):
            inc = args["increase_sound_args"]["inc"]
            wave_data = speech_task_func.increase_sound(wave_data, inc)

        wave_data.export(output_path)
        message = "success"
        code    = 1
    except Exception as e:
        code    = 3
        message = f"{e}"
    return code, message