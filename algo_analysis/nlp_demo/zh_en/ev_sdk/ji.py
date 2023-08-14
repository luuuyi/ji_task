import os
import os.path as osp
import json
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer, AutoModelForSeq2SeqLM

def init():
    """Initialize model, implemented by algo developer, called by upper application
    Returns: model
    """
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    translation = pipeline("translation_zh_to_en", model=model, tokenizer=tokenizer)
    return {
        "model": model,
        "tokenizer": tokenizer,
        "translation": translation
    }

def process(model=None, input_data=None, args=None, ** kwargs):
    """Do inference and get output, implemented by algo developer, called by upper application
    Returns: process json result
    """
    # Process here
    translation = model["translation"]
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
    del model["model"]
    del model["tokenizer"]
    del model["translation"]
    del model

if __name__ == "__main__":
    model_info = init()
    input_data = "学生住宿中心,度假屋"
    args = {
        "algo_type":"NLP"
    }
    results = process(model=model_info, input_data=input_data, args=args)
    print(results)
    uninit(model_info)