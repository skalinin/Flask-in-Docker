import requests
import json
import cv2
import time

from src.utils import encode_image, decode_image

start_time = time.time()

url = 'http://185.244.175.57:399/rotate'
# url = 'http://172.17.0.2:399/rotate'

img = cv2.imread('picture.jpg')
img_b64 = encode_image(img)
data = {"image": img_b64, "other_key": "value"}

response = requests.post(url=url, json=data)

data = response.json()
img_b64 = data['image']
img = decode_image(img_b64)
cv2.imwrite('pred.jpg', img)

print(time.time() - start_time)
