import cv2
import numpy as np
import random

from cv_task.ace import zmIceColor

def fill_old(imga, imgb, roi):
    assert imga.shape[-1] == 3, imga.shape
    # check valid
    assert len(roi) == 4, roi
    assert (roi[0] <= roi[2]) and (roi[1] <= roi[3]), roi

    h_a, w_a, c_a = imga.shape
    h_b, w_b, c_b = imga.shape
    # roi区域不超过图片的范围
    assert roi[0] >= 0 and roi[0] < w_a
    assert roi[2] >= 0 and roi[2] < w_a
    assert roi[1] >= 0 and roi[1] < h_a
    assert roi[3] >= 0 and roi[3] < h_a

    # function
    roi_w, roi_h = roi[2] - roi[0], roi[3] - roi[1]
    imgb_s = cv2.resize(imgb, (roi_w, roi_h))
    imga[roi[1]:roi[3], roi[0]:roi[2]] = imgb_s
    return imga

def fill(imga, wh):
    assert imga.shape[-1] == 3, imga.shape
    # check valid
    assert len(wh) == 2, wh

    h_a, w_a, c_a = imga.shape
    w_t, h_t      = wh
    if h_a >= h_t and w_a >= w_t:
        return imga

    zeros_img = np.zeros((h_t, w_t, c_a), imga.dtype)
    zeros_img[:h_a, :w_a, ...] = imga

    return zeros_img

def hist_equa(img):
    # https://www.jb51.net/article/264125.htm
    assert img.shape[-1] == 3, img.shape

    # 直方图均衡化
    # equ = cv2.equalizeHist(img)
    # 自适应直方图均衡化
    # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    # res_clahe = clahe.apply(img)

    # 获取每个通道的数据
    r_channel, g_channel, b_channel = cv2.split(img)
    # 对 L 通道进行直方图均衡化
    r_channel = cv2.equalizeHist(r_channel)
    g_channel = cv2.equalizeHist(g_channel)
    b_channel = cv2.equalizeHist(b_channel)
    # 合并各通道
    lab_img = cv2.merge((r_channel, g_channel, b_channel))

    return lab_img

def white_balance(img):
    # https://www.yzktw.com.cn/post/1236714.html
    assert img.shape[-1] == 3, img.shape

    lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    # 获取每个通道的数据
    l_channel, a_channel, b_channel = cv2.split(lab_img)
    # 对 L 通道进行直方图均衡化
    l_channel = cv2.equalizeHist(l_channel)
    # 合并各通道
    lab_img = cv2.merge((l_channel, a_channel, b_channel))
    # 将 LAB 颜色空间转为 RGB 颜色空间
    result = cv2.cvtColor(lab_img, cv2.COLOR_LAB2BGR)
    return result

def automatic_color_enhancement(img):
    # https://blog.51cto.com/u_13984132/5651065
    # http://681314.com/A/ptObLhFM40
    assert img.shape[-1] == 3, img.shape
    res = zmIceColor(img / 255.0) * 255
    return res

def blur(img, kernel_size=5):
    assert img.shape[-1] == 3, img.shape

    #定义滤波核大小
    size = kernel_size

    #均值滤波降低图像噪声
    blurImg = cv2.blur(img, (size, size))
 
    return blurImg

if __name__ == "__main__":
    imga = cv2.imread("test.jpeg", -1)
    imgb = cv2.imread("test.jpeg", -1)
    save_img = "result.jpeg"
    import ipdb; ipdb.set_trace()

    # No.1
    # roi = [100, 100, 200, 200]
    # ret_image = fill_old(imga, imgb, roi)
    # cv2.imwrite(save_img, ret_image)

    # No.2
    # ret_image = hist_equa(imga)
    # cv2.imwrite(save_img, ret_image)

    # No.3
    # ret_image = white_balance(imga)
    # cv2.imwrite(save_img, ret_image)

    # No.4
    # ret_image = automatic_color_enhancement(imga)
    # cv2.imwrite(save_img, ret_image)

    # No.5
    # ret_image = blur(imga)
    # cv2.imwrite(save_img, ret_image)

    # No.6
    wh = [2000, 2000]
    ret_image = fill(imga, wh)
    cv2.imwrite(save_img, ret_image)