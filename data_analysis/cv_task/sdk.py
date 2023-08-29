import cv2
import cv_task.func as cv_task_func

def call_cv_task(imga_path, output_path, args):
    try:
        imga = cv2.imread(imga_path, -1)

        # No.1
        if args.get("fill_flag", 0):
            roi = args["fill_args"]["roi"]
            imga = cv_task_func.fill(imga, roi)
            # if config["save_result"]:
            #     save_img = f"result_fill.jpeg"
            #     cv2.imwrite(save_img, imga)

        # No.2
        if args.get("hist_equa_flag", 0):
            imga = cv_task_func.hist_equa(imga)
            # if config["save_result"]:
            #     save_img = f"result_hist_equa.jpeg"
            #     cv2.imwrite(save_img, imga)

        # No.3
        if args.get("white_balance_flag", 0):
            imga = cv_task_func.white_balance(imga)
            # if config["save_result"]:
            #     save_img = f"result_white_balance.jpeg"
            #     cv2.imwrite(save_img, imga)

        # No.4
        if args.get("automatic_color_enhancement_flag", 0):
            imga = cv_task_func.automatic_color_enhancement(imga)
            # if config["save_result"]:
            #     save_img = f"result_automatic_color_enhancement.jpeg"
            #     cv2.imwrite(save_img, imga)

        # No.5
        if args.get("blur_flag", 0):
            imga = cv_task_func.blur(imga)
            # if config["save_result"]:
            #     save_img = f"result_blur.jpeg"
            #     cv2.imwrite(save_img, imga)

        cv2.imwrite(output_path, imga)
        message = "success"
        code    = 1
    except Exception as e:
        code    = 2
        message = f"{e}"

    return code, message