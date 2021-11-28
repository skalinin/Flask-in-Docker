import numpy as np
import cv2
import base64


def encode_image(img):
    """Encode image to base64.
    https://jdhao.github.io/2020/03/17/base64_opencv_pil_image_conversion/
    """
    _, img_encoded = cv2.imencode('.jpg', img)
    img_b64 = base64.b64encode(img_encoded).decode('utf-8')
    return img_b64


def decode_image(img_b64):
    """Decode image from base64.
    https://jdhao.github.io/2020/03/17/base64_opencv_pil_image_conversion/
    """
    img_bytes = base64.b64decode(img_b64)
    im_arr = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img
