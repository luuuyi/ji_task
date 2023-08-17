EV_ALGORITHM_TEST_TASK_ID  = 123
EV_TEST_MESSAGE_SAVE_PATH  = "/app/test/test_id/result.json"
EV_AUTO_TEST_CONFIG_PARAMS = \
    '''
    {
        "input_path": "/root/input_dataset",
        "output_path":"/root/output_dataset",
        "data_set_type":"NLP",
        "data_set_format":"plain text",
        "pretreatment_flag":1,
        "pretreatment": {
            "fill_flag": 1,
            "fill_args": {"roi": [100, 100, 200, 200]},

            "hist_equa_flag": 1,
            "white_balance_flag": 1,
            "automatic_color_enhancement_flag": 1,
            "blur_flag": 1,

            "remove_number_flag": 1,
            "remove_space_flag": 1,
            "remove_url_flag": 1,
            "remove_duplicate_str_flag": 1,

            "denoise_flag": 1,
            "remove_silence_flag": 1,
            "increase_sound_flag": 1,
            "increase_sound_args": {"inc": 10}
        }
    }
    '''
EV_AUTO_TEST_DEVICE        = "nvidia"

RET_JSON = \
    '''
    {
        "code": 1,
        "message": "template",
        "data": {"status": 0},
        "id": 66
    }
    '''