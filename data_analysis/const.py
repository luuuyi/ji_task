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
        "pretreatment": {'cut_size_flag': 1,
                    'cut_size': {'cut_start_x': 10, 'cut_start_y': 10, 'cut_end_x': 110, 'cut_end_y': 110,
                                    'org_height': 512, 'org_width': 512},
                    'random_rotation_flag': 1, 
                    'random_rotation': {'lower_limit': 0, 'upper_limit': 10},
                    'random_scale_flag': 1, 
                    'random_scale': {'lower_limit': 0, 'upper_limit': 10},
                    'random_translation_flag': 1,
                    'random_translation': {'x_lower_limit': 0, 'x_upper_limit': 10, 'y_lower_limit': 0,
                                            'y_upper_limit': 10},
                    'flip_horizontal': 1, 
                    'mirror_flip': 3,
                    'limitation_line_transformation_flag': 1, 
                    'limitation_line_transformation': {'x': 5, 'y': 5},
                    'picture_noice': {'salt': 1, 'gaussian': 1, 'white_gaussian': 1, 'poisson': 1, 'multiplicative': 1},
                    'dimming_flag': 1, 
                    'dimming': 0.5,
                    'picture_contrast_flag': 1, 
                    'picture_contrast': 0.5,
                    'picture_sharp_flag': 1, 
                    'picture_sharp': 0.5}
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