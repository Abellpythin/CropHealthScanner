def get_treatment_recommendations(disease):
    """
    Get treatment recommendations based on the diagnosed disease
    """
    # Treatment recommendations database
    treatments = {
        "Healthy": [
            "Continue regular maintenance",
            "Monitor for any changes",
            "Follow regular watering schedule"
        ],
        "Leaf Blight": [
            "Remove and destroy infected leaves",
            "Apply appropriate fungicide",
            "Improve air circulation around plants",
            "Avoid overhead watering"
        ],
        "Powdery Mildew": [
            "Apply sulfur-based fungicide",
            "Increase plant spacing for better air flow",
            "Water at the base of plants",
            "Remove severely infected plants"
        ],
        "Rust Disease": [
            "Apply rust-specific fungicide",
            "Remove infected plant material",
            "Maintain proper plant spacing",
            "Avoid wet leaves overnight"
        ],
        "Leaf Spot": [
            "Apply copper-based fungicide",
            "Remove affected leaves",
            "Improve drainage",
            "Rotate crops in future seasons"
        ]
    }
    
    return treatments.get(disease, [
        "Consult an agricultural expert",
        "Monitor plant condition",
        "Document symptoms for expert analysis"
    ])
