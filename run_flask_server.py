import flask
import argparse

from src.model import Model
from src.utils import encode_image, decode_image


app = flask.Flask(__name__)


@app.route('/rotate', methods=['POST'])
def rotate_image():
    r = flask.request
    img_b64 = r.json['image']
    img = decode_image(img_b64)

    img = MODEL(img)

    img_b64 = encode_image(img)
    data = {"image": img_b64, "other_key": "value"}
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=399,
                        help='Flask server port.')
    args = parser.parse_args()

    MODEL = Model()
    app.run(host="0.0.0.0", port=args.port)
