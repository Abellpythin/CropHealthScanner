import numpy as np
from sklearn.ensemble import RandomForestClassifier
from image_processor import extract_features

# Initialize classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Define disease classes
DISEASE_CLASSES = [
    "Healthy",
    "Leaf Blight",
    "Powdery Mildew",
    "Rust Disease",
    "Leaf Spot"
]

def initialize_model():
    """
    Initialize the model with basic parameters
    Note: In production, this would load a pre-trained model
    """
    global model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    # In production: model.load_weights('path_to_weights')

def predict_disease(processed_image):
    """
    Predict the disease from the processed image
    Args:
        processed_image: Numpy array of processed image
    Returns:
        prediction: String name of predicted disease
        confidence: Float confidence score
    """
    # Extract image features
    features = extract_features(processed_image)
    features = features.reshape(1, -1)

    # For demonstration: simulate prediction
    # In production, this would use actual model prediction
    prediction_idx = np.random.randint(0, len(DISEASE_CLASSES))
    confidence = np.random.uniform(70, 95)

    return DISEASE_CLASSES[prediction_idx], confidence