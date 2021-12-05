import cv2
import time
import numpy as np
import sys
from PIL import ImageFont, ImageDraw, Image

WORK_DIR_PATH = "/home/user/UI_ENG_for_python/"         #工作資料夾路徑
FONT_PATH = WORK_DIR_PATH + "NotoSansCJKtc-Bold.otf"    #字型檔
GENERATED_IMG_NAME = WORK_DIR_PATH + "frame.png"        #輸出檔案名稱


def pasteImg(img, overlay, x, y):
    y1, y2 = y, y + overlay.shape[0]
    x1, x2 = x, x + overlay.shape[1]

    alpha_s = overlay[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img[y1:y2, x1:x2, c] = (alpha_s * overlay[:, :, c] +
                                alpha_l * img[y1:y2, x1:x2, c])

if sys.argv[1] == "1":
    img = cv2.imread("01.png")
else:
    string = "0" + sys.argv[1] + ".png"
    print (string)
    img = cv2.imread(string)

    if sys.argv[1] == "5":
        cv2.rectangle(img,(0,600),(768,800),(255,255,255),-1)
        
        if len(sys.argv) == 4:
            if sys.argv[3] == "0":
                print("left")
                left_select_button = cv2.imread("selectTime_reduce_selected.png", -1)
                right_select_button = cv2.imread("selectTime_add_select.png", -1)
            elif sys.argv[3] == "1":
                print("right")
                left_select_button = cv2.imread("selectTime_reduce_select.png", -1)
                right_select_button = cv2.imread("selectTime_add_selected.png", -1)
        else:
            left_select_button = cv2.imread("selectTime_reduce_select.png", -1)
            right_select_button = cv2.imread("selectTime_add_select.png", -1)

        pasteImg(img, right_select_button, 500, 630)
        pasteImg(img, left_select_button, 150, 630)
        font = ImageFont.truetype(FONT_PATH, 100)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        text = str(int(sys.argv[2])*0.5)
        w, h = draw.textsize(text, font)
        draw.text(((768-w)/2, 600),  text, font = font, fill = (152,179,0, 0))
        img = np.array(img_pil)
        
    
    

    cv2.rectangle(img,(0,1024-69),(768,1024),(152,179,0),-1)

    
    font = ImageFont.truetype(FONT_PATH, 45)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    text = time.strftime("%Y-%m-%d %H:%M", time.localtime())

    w, h = draw.textsize(text, font)

    draw.text(((768-w)/2, (1024-69)),  text, font = font, fill = (255, 255, 255, 0))

    img = np.array(img_pil)


cv2.imwrite(GENERATED_IMG_NAME, img)