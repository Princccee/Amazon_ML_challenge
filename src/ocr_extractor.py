import numpy as np
from paddleocr import PaddleOCR

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en', use_gpu=True)  # Using GPU by default

def extract_text_from_image(image):
    if image is not None:
        image_np = np.array(image)
        result = ocr.ocr(image_np, cls=True)
        if result and result[0]:
            text = ' '.join([line[1][0] for line in result[0]])
            return text
    return ''