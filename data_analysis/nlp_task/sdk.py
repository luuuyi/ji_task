import nlp_task.func as nlp_task_func

def call_nlp_task(input_path, output_path, args):
    try:
        str_list = list()
        with open(input_path, "r", encoding="utf-8") as fin:
            for line in fin.readlines():
                str_list.append(line.rstrip())

        # import ipdb; ipdb.set_trace()
        print(f"[{input_path}] find {len(str_list)} string")
        # No.1
        if args["remove_number_flag"]:
            str_list = [nlp_task_func.remove_number(t) for t in str_list]

        # No.2
        if args["remove_space_flag"]:
            str_list = [nlp_task_func.remove_space(t) for t in str_list]

        # No.3
        if args["remove_url_flag"]:
            str_list = [nlp_task_func.remove_url(t) for t in str_list]
        
        # No.4
        if args["remove_duplicate_str_flag"]:
            str_list = nlp_task_func.remove_duplicate_str(str_list)

        # No.5
        words = args["remove_words_args"]["words"]
        if args["remove_words_flag"]:
            str_list = [nlp_task_func.remove_words(t, words) for t in str_list]

        with open(output_path, "w", encoding="utf-8") as fout:
            fout.writelines(str_list)
        message = "success"
        code    = 1
    except Exception as e:
        code    = 2
        message = f"{e}"
    return code, message