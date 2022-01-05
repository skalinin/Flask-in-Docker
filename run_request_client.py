import argparse
import requests
import json
import cv2
import os

from src.utils import encode_image, decode_image


def main(args):
    os.makedirs(args.save_dir, exist_ok=True)
    url = f'http://{args.ip}:{args.port}/rotate'
    img = cv2.imread(args.path_to_image)
    img_b64 = encode_image(img)
    data = {"image": img_b64, "other_key": "value"}

    response = requests.post(url=url, json=data)

    data = response.json()
    img_b64 = data['image']
    img = decode_image(img_b64)

    img_name = os.path.basename(args.path_to_image)
    save_path = os.path.join(args.save_dir, img_name)
    cv2.imwrite(save_path, img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str,
                        help='Server ip address.')
    parser.add_argument('--port', type=int, default=399,
                        help='Server port.')
    parser.add_argument('--path_to_image', type=str,
                        default='/workdir/data/picture.jpg',
                        help='Path to input image.')
    parser.add_argument('--save_dir', type=str,
                        default='/workdir/data/pred/',
                        help='Dir to folder to save predicted images.')
    args = parser.parse_args()

    main(args)
