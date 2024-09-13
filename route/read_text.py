import numpy as np
import cv2
from flask import Blueprint, Response, json, request
from utility import constant
from service import ocr_service


read_text_bp = Blueprint('read_text', __name__)


@read_text_bp.route(rule='/', methods=['POST'])
def api_welcome():
    welcome = {'code': 200, 'message': 'success', 'data': 'Welcome to read text API'}
    return Response(response=json.dumps(welcome), **constant.RES_PARAM)


@read_text_bp.route(rule='/read-text', methods=['POST'])
def read_text():
    # Check content_type
    if not request.content_type.startswith("multipart/form-data"):
        res = {'code': 400, 'message': 'Content type must be multipart/form-data', 'data': None}
    # Check for image
    elif 'image' not in request.files:
        res = {'code': 400, 'message': 'No image', 'data': None}
    else:
        # Read image
        arr = np.fromstring(request.files["image"].read(), np.uint8)
        image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        if image is None:
            res = {'code': 400, 'message': 'Cannot read image', 'data': None}
        else:
            res = {'code': 200, 'message': 'Success', 'data': ocr_service.read_text(image)}
    return Response(response=json.dumps(res), **constant.RES_PARAM)
