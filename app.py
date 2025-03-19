import streamlit as st
import numpy as np
from PIL import Image
import io
from image_processor import process_image
from model_handler import predict_disease
from utils import get_treatment_recommendations

def main():
    # Set up the main page title and description
    st.title("Crop Disease Diagnosis Tool")

    # Display user instructions
    st.write("""
    Upload a photo of your crop to get instant disease diagnosis and treatment recommendations.
    For best results:
    - Ensure good lighting
    - Focus on affected areas
    - Avoid blurry images
    """)

    # Create the file uploader component
    uploaded_file = st.file_uploader(
        "Choose an image of your crop",
        type=['jpg', 'jpeg', 'png']
    )

    if uploaded_file is not None:
        try:
            # Load and display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_container_width=True)

            # Add analyze button and process image when clicked
            if st.button('Analyze Image'):
                with st.spinner('Analyzing image...'):
                    # Process the image for analysis
                    processed_image = process_image(image)

                    # Get disease prediction and confidence score
                    prediction, confidence = predict_disease(processed_image)

                    # Display the diagnosis results
                    st.subheader("Diagnosis Results")
                    st.write(f"Detected Issue: {prediction}")
                    st.write(f"Confidence: {confidence:.2f}%")

                    # Get and display treatment recommendations
                    recommendations = get_treatment_recommendations(prediction)
                    st.subheader("Treatment Recommendations")
                    for idx, rec in enumerate(recommendations, 1):
                        st.write(f"{idx}. {rec}")

                    # Display disclaimer
                    st.info("Note: This is a preliminary diagnosis. For severe cases, please consult an agricultural expert.")

        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")
            st.write("Please try uploading a different image or check if the image is corrupted.")

if __name__ == "__main__":
    main()