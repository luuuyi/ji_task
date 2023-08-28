import os
import os.path as osp
import json
import shutil
import zipfile

import const
import cv_task.sdk as cv_sdk
import nlp_task.sdk as nlp_sdk
import speech_task.sdk as speech_sdk

def _process_cv(tmp_input_dir, tmp_output_dir, args):
    ret_json = json.loads(const.RET_JSON)
    message, code = "success", 1

    file_list = list()
    
    # for _file in os.listdir(tmp_input_dir):
    #     full_path = osp.join(tmp_input_dir, _file)
    #     suffix = _file.split(".")[-1].lower()
    #     if suffix not in const.CV_SUFFIX:
    #         print(f"skip {full_path}")
    #         continue
    #     file_list.append(full_path)

    for root, dirs, files in os.walk(tmp_input_dir):
        for _file in files:
            full_path = osp.join(root, _file)
            suffix = _file.split(".")[-1].lower()
            if suffix not in const.CV_SUFFIX:
                print(f"skip {full_path}")
                continue
            file_list.append(full_path)

    print(f"find {len(file_list)} files")
    out_file_list = list()
    for input_path in file_list:
        print(f"process {input_path}")
        output_path = input_path.replace(tmp_input_dir, tmp_output_dir)
        output_dir = osp.dirname(output_path)
        if not osp.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        code, message = cv_sdk.call_cv_task(input_path, output_path, args)
        if code != 1:
            break
        out_file_list.append(output_path)

    ret_json["code"]    = code
    ret_json["message"] = message
    ret_json["id"]      = os.environ.get("EV_ALGORITHM_TEST_TASK_ID")
    return ret_json, out_file_list

def _process_nlp(tmp_input_dir, tmp_output_dir, args):
    ret_json = json.loads(const.RET_JSON)
    message, code = "success", 1

    file_list = list()
    for root, dirs, files in os.walk(tmp_input_dir):
        for _file in files:
            full_path = osp.join(root, _file)
            suffix = _file.split(".")[-1].lower()
            if suffix not in const.NLP_SUFFIX:
                print(f"skip {full_path}")
                continue
            file_list.append(full_path)

    print(f"find {len(file_list)} files")
    out_file_list = list()
    for input_path in file_list:
        print(f"process {input_path}")
        output_path = input_path.replace(tmp_input_dir, tmp_output_dir)
        output_dir = osp.dirname(output_path)
        if not osp.exists(output_dir):
            os.makedirs(output_dir)
        code, message = nlp_sdk.call_nlp_task(input_path, output_path, args)
        if code != 1:
            break
        out_file_list.append(output_path)

    ret_json["code"]    = code
    ret_json["message"] = message
    ret_json["id"]      = os.environ.get("EV_ALGORITHM_TEST_TASK_ID")
    return ret_json, out_file_list

def _process_speech(tmp_input_dir, tmp_output_dir, args):
    ret_json = json.loads(const.RET_JSON)
    message, code = "success", 1

    file_list = list()
    for root, dirs, files in os.walk(tmp_input_dir):
        for _file in files:
            full_path = osp.join(root, _file)
            suffix = _file.split(".")[-1].lower()
            if suffix not in const.SPEECH_SUFFIX:
                print(f"skip {full_path}")
                continue
            file_list.append(full_path)

    print(f"find {len(file_list)} files")
    out_file_list = list()
    for input_path in file_list:
        print(f"process {input_path}")
        output_path = input_path.replace(tmp_input_dir, tmp_output_dir)
        output_dir = osp.dirname(output_path)
        if not osp.exists(output_dir):
            os.makedirs(output_dir)
        code, message = speech_sdk.call_speech_task(input_path, output_path, args)
        if code != 1:
            break
        out_file_list.append(output_path)

    ret_json["code"]    = code
    ret_json["message"] = message
    ret_json["id"]      = os.environ.get("EV_ALGORITHM_TEST_TASK_ID")
    return ret_json, out_file_list

def process_interface(args):
    print(f"current config: {args}")
    env_args = os.environ.get("EV_AUTO_TEST_CONFIG_PARAMS")
    if env_args:
        print(f"use env EV_AUTO_TEST_CONFIG_PARAMS to update args")
        args = env_args
    else:
        print(f"detect no env args!")
    print(f"after read env, config is: {args}")
    device = os.environ.get("EV_AUTO_TEST_DEVICE")
    print(f"runtime device is: {device}")

    assert "input_path" in args and args["input_path"].endswith(".zip"), args
    assert "output_path" in args and args["output_path"].endswith(".zip"), args
    assert "data_set_type" in args and args["data_set_type"] in ("NLP", "SPEECH", "CV"), args
    assert "pretreatment" in args and isinstance(args["pretreatment"], dict), args

    tmp_input_dir, tmp_output_dir = const.TMP_INPUT_DIR, const.TMP_OUTPUT_DIR
    if osp.exists(tmp_input_dir):
        shutil.rmtree(tmp_input_dir)
    os.makedirs(tmp_input_dir)
    if osp.exists(tmp_output_dir):
        shutil.rmtree(tmp_output_dir)
    os.makedirs(tmp_output_dir)

    with zipfile.ZipFile(args["input_path"], "r") as zip_ref:
        zip_ref.extractall(tmp_input_dir)

    if args["data_set_type"] == "CV":
        ret_json, out_file_list = _process_cv(tmp_input_dir, tmp_output_dir, args["pretreatment"])
    elif args["data_set_type"] == "NLP":
        ret_json, out_file_list = _process_nlp(tmp_input_dir, tmp_output_dir, args["pretreatment"])
    elif args["data_set_type"] == "SPEECH":
        ret_json, out_file_list = _process_speech(tmp_input_dir, tmp_output_dir, args["pretreatment"])
    
    ret_file = os.environ.get("EV_TEST_MESSAGE_SAVE_PATH")
    ret_dir  = osp.dirname(ret_file)
    print(f"ret_file: {ret_file}; ret_dir: {ret_dir}")
    if not osp.exists(ret_dir):
        print(f"{ret_dir} not exists, create it!")
        os.makedirs(ret_dir)
    with open(ret_file, "w", encoding="utf-8") as fout:
        json.dump(ret_json, fout, indent=2, ensure_ascii=False)

    with zipfile.ZipFile(args["output_path"], "w") as zip_ref:
        for _file in out_file_list:
            zip_ref.write(_file)
    return ret_file

if __name__ == "__main__":
    args = {
        "input_path": "./tmp/input_dataset.zip",
        "output_path":"./tmp/output_dataset.zip",
        "data_set_type":"SPEECH",
        "data_set_format":"plain text",
        "pretreatment_flag":1,
        "pretreatment": {
            "fill_flag": 1,
            "fill_args": {"roi": [500, 500]},
            "hist_equa_flag": 1,
            "white_balance_flag": 1,
            "automatic_color_enhancement_flag": 1,
            "blur_flag": 1,

            "remove_number_flag": 1,
            "remove_space_flag": 1,
            "remove_url_flag": 1,
            "remove_duplicate_str_flag": 1,
            "remove_words_flag": 1,
            "remove_words_args": {"words": ["hello", ]},


            "denoise_flag": 1,
            "remove_silence_flag": 1,
            "increase_sound_flag": 1,
            "increase_sound_args": {"inc": 10}
        }
    }
    ret_file = process_interface(args)
    with open(ret_file, "r", encoding="utf-8") as fin:
        infos = json.load(fin)
    print(infos)