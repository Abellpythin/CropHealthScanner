import numpy as np
from sklearn.ensemble import RandomForestClassifier
from image_processor import extract_features

# Initialize a basic model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Predefined classes for common crop diseases
DISEASE_CLASSES = [
    "Healthy",
    "Leaf Blight",
    "Powdery Mildew",
    "Rust Disease",
    "Leaf Spot"
]

def initialize_model():
    """
    Initialize the model with some basic parameters
    Note: In a production environment, this would load a pre-trained model
    """
    # For demonstration, we're using a simple random forest
    # This should be replaced with a properly trained model in production
    global model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # In production, you would load actual trained weights here
    # model.load_weights('path_to_weights')

def predict_disease(processed_image):
    """
    Predict the disease from the processed image
    """
    # Extract features from the image
    features = extract_features(processed_image)
    
    # Reshape features for prediction
    features = features.reshape(1, -1)
    
    # In a real implementation, this would use the actual trained model
    # For now, we'll return a simplified prediction
    # This should be replaced with actual model prediction in production
    
    # Simulate prediction (remove in production)
    prediction_idx = np.random.randint(0, len(DISEASE_CLASSES))
    confidence = np.random.uniform(70, 95)
    
    return DISEASE_CLASSES[prediction_idx], confidence
