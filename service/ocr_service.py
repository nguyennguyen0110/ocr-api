import pytesseract
from unidecode import unidecode


def read_text(image):
    """
    Detect and read all the text from image and return them in accents form and decoded form, with their
    positions.
    :param image: image to read text
    :return: all text and position
    """
    # Detect text in image
    detected_texts = pytesseract.image_to_string(image, lang='vie_price_tag')
    # Initialize some list to contain information
    texts = []
    decoded_texts = []
    for text in detected_texts.split('\n'):
        if len(text) == 0:
            continue
        texts.append(text)
        decoded_texts.append(unidecode(text))
    return {'texts': texts, 'decoded_texts': decoded_texts}
