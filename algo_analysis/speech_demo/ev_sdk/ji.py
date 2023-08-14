import os
import os.path as osp
import json
import requests

PROJECT_PATH = "path/to/init_task"

import sys
sys.path.insert(0, PROJECT_PATH)

from masr.predict import MASRPredictor

def init():
    """Initialize model, implemented by algo developer, called by upper application
    Returns: model
    """
    predictor = MASRPredictor(model_tag='conformer_streaming_fbank_aishell')
    return {
        "predictor": predictor
    }

def process(model=None, input_data=None, args=None, ** kwargs):
    """Do inference and get output, implemented by algo developer, called by upper application
    Returns: process json result
    """
    # Process here
    predictor = model["predictor"]
    input_data = requests.get(input_data).content
    result = predictor.predict(audio_data=input_data, use_pun=False)
    score, text = result['score'], result['text']

    results = {
        "code": 0,
        "output_data":
        {
            "result": text
        }
    }
    results = json.dumps(results, indent=4, ensure_ascii=False)

    return results

def uninit(model=None):
    """release resources, implemented by algo developer, called by upper application
    do release resources if necessary
    """
    del model["predictor"]
    del model

if __name__ == "__main__":
    model_info = init()
    wav_file = osp.join(PROJECT_PATH, "dataset/test.wav")
    args = {
        "algo_type":"SPEECH"
    }
    results = process(model=model_info, input_data=wav_file, args=args)
    print(results)
    uninit(model_info)