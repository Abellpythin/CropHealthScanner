import cv2
import numpy as np
from PIL import Image

def process_image(pil_image):
    """
    Process the uploaded image for analysis
    Args:
        pil_image: PIL Image object uploaded by user
    Returns:
        processed_image: Numpy array of processed image
    """
    # Convert PIL image to numpy array
    image = np.array(pil_image)

    # Convert RGBA to RGB if needed
    if image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)

    # Resize image to standard size for model
    image = cv2.resize(image, (224, 224))

    # Apply Gaussian blur to reduce noise
    image = cv2.GaussianBlur(image, (3, 3), 0)

    # Normalize pixel values to [0,1] range
    image = image / 255.0

    return image

def extract_features(processed_image):
    """
    Extract relevant features from the processed image
    Args:
        processed_image: Numpy array of processed image
    Returns:
        features: Array of extracted image features
    """
    # Convert to HSV color space for better color analysis
    hsv = cv2.cvtColor(processed_image.astype(np.float32), cv2.COLOR_RGB2HSV)

    # Calculate color histograms for each channel
    hist_h = cv2.calcHist([hsv], [0], None, [32], [0, 1]).flatten()
    hist_s = cv2.calcHist([hsv], [1], None, [32], [0, 1]).flatten()
    hist_v = cv2.calcHist([hsv], [2], None, [32], [0, 1]).flatten()

    # Normalize histograms
    hist_h = cv2.normalize(hist_h, hist_h).flatten()
    hist_s = cv2.normalize(hist_s, hist_s).flatten()
    hist_v = cv2.normalize(hist_v, hist_v).flatten()

    # Combine all features
    features = np.concatenate([hist_h, hist_s, hist_v])

    return features