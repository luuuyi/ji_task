import os
import os.path as osp
import json
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer, AutoModelForSeq2SeqLM

def init():
    """Initialize model, implemented by algo developer, called by upper application
    Returns: model
    """
    ez_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh", local_files_only=True, revision=None)
    ez_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh", local_files_only=True, revision=None)
    ez_translation = pipeline("translation_en_to_zh", model=ez_model, tokenizer=ez_tokenizer)

    ze_model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en", local_files_only=True, revision=None)
    ze_tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en", local_files_only=True, revision=None)
    ze_translation = pipeline("translation_zh_to_en", model=ze_model, tokenizer=ze_tokenizer)
    return {
        "ez_model": ez_model,
        "ez_tokenizer": ez_tokenizer,
        "ez_translation": ez_translation,

        "ze_model": ze_model,
        "ze_tokenizer": ze_tokenizer,
        "ze_translation": ze_translation,
    }

def process(model=None, input_data=None, args=None, ** kwargs):
    """Do inference and get output, implemented by algo developer, called by upper application
    Returns: process json result
    """
    # Process here
    if (input_data[0] >= "a" and input_data[0] <= "z") or (input_data[0] >= "A" and input_data[0] <= "Z"):
        print("english to chinese mode")
        translation = model["ez_translation"]
    else:
        print("chinese to english mode")
        translation = model["ze_translation"] 

    translated_text = translation(input_data, max_length=40)[0]['translation_text']
    results = {
        "code": 0,
        "output_data":
        {
            "result": translated_text
        }
    }
    results = json.dumps(results, indent=4, ensure_ascii=False)

    return results

def uninit(model=None):
    """release resources, implemented by algo developer, called by upper application
    do release resources if necessary
    """
    del model["ez_model"]
    del model["ez_tokenizer"]
    del model["ez_translation"]

    del model["ze_model"]
    del model["ze_tokenizer"]
    del model["ze_translation"]

    del model

if __name__ == "__main__":
    model_info = init()
    input_data = "Student accommodation centres, resorts"
    args = {
        "algo_type":"NLP"
    }
    results = process(model=model_info, input_data=input_data, args=args)
    print(results)
    uninit(model_info)