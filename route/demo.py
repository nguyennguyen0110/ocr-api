import numpy as np
import cv2
from flask import Blueprint, render_template, request
from service import ocr_service


demo_bp = Blueprint('demo', __name__)


@demo_bp.route(rule='/', methods=['GET', 'POST'])
def read_text():
    if request.method == 'POST':
        if not request.content_type.startswith("multipart/form-data"):
            result = {'code': 400, 'message': 'Content type must be multipart/form-data', 'data': None}
            # Check for image
        elif 'image' not in request.files:
            result = {'code': 400, 'message': 'No image', 'data': None}
        else:
            # Read image
            arr = np.fromstring(request.files["image"].read(), np.uint8)
            image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
            if image is None:
                result = {'code': 400, 'message': 'Cannot read image', 'data': None}
            else:
                result = {'code': 200, 'message': 'Success', 'data': ocr_service.read_text(image)}
    else:
        result = {}
    return render_template('read_text.html', result=result)
