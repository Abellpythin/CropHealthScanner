# Crop Disease Diagnosis Tool

A mobile-friendly web application that helps farmers diagnose crop diseases using image analysis and provides treatment recommendations.

## Features

- Image upload and processing
- Disease detection
- Treatment recommendations
- Mobile-friendly interface

## Components

### 1. Image Processing (`image_processor.py`)
Handles image preprocessing using OpenCV:
- Resizes images to standard size (224x224)
- Applies Gaussian blur for noise reduction
- Normalizes pixel values
- Extracts color features using HSV histograms

### 2. Disease Detection (`model_handler.py`)
Manages the disease classification model:
- Uses RandomForest classifier for disease prediction
- Supported diseases:
  - Healthy
  - Leaf Blight
  - Powdery Mildew
  - Rust Disease
  - Leaf Spot
- Provides confidence scores for predictions

### 3. Treatment Recommendations (`utils.py`)
Contains disease-specific treatment recommendations:
- Customized treatment plans for each disease
- General maintenance advice
- Preventive measures
- Expert consultation recommendations

### 4. Main Application (`app.py`)
Streamlit-based user interface:
- Image upload functionality
- Real-time disease analysis
- Treatment display
- Error handling

## Usage Instructions

1. **Starting the Application**
   ```bash
   streamlit run app.py --server.port 5000
   ```

2. **Using the Interface**
   - Upload an image using the file uploader
   - Click "Analyze Image" to process
   - View results and recommendations
   
3. **Image Guidelines**
   - Use clear, well-lit images
   - Focus on affected areas
   - Avoid blurry photos
   - Supported formats: JPG, JPEG, PNG

## Technical Requirements

- Python 3.11
- Required packages:
  - streamlit
  - opencv-python
  - numpy
  - pillow
  - scikit-learn

## File Structure

```
├── app.py                 # Main Streamlit application
├── image_processor.py     # Image processing functions
├── model_handler.py       # Disease classification model
├── utils.py              # Treatment recommendations
└── .streamlit/           # Streamlit configuration
    └── config.toml       # Server settings
```

## Configuration

The `.streamlit/config.toml` contains server settings:
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000
```

## Development Notes

- The application uses a simplified model for demonstration
- In production, replace the random predictions with a trained model
- Error handling is implemented for corrupted images and processing failures
- The interface is optimized for mobile devices

## Future Enhancements

- Advanced ML models for better accuracy
- Image history and diagnosis tracking
- Detailed treatment plan database
