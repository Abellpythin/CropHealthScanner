import streamlit as st
import numpy as np
from PIL import Image
import io
import os
from datetime import datetime
from image_processor import process_image
from model_handler import predict_disease
from utils import get_treatment_recommendations
from database import save_diagnosis, get_recent_diagnoses

def save_uploaded_image(uploaded_file):
    """Save uploaded image and return the path"""
    # Create images directory if it doesn't exist
    if not os.path.exists('uploaded_images'):
        os.makedirs('uploaded_images')

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}.jpg"
    file_path = os.path.join('uploaded_images', filename)

    # Save the file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

def main():
    st.title("Crop Disease Diagnosis Tool")

    # Add tabs for upload and history
    tab1, tab2 = st.tabs(["Diagnose", "History"])

    with tab1:
        st.write("""
        Upload a photo of your crop to get instant disease diagnosis and treatment recommendations.
        For best results:
        - Ensure good lighting
        - Focus on affected areas
        - Avoid blurry images
        """)

        # Image upload
        uploaded_file = st.file_uploader("Choose an image of your crop", type=['jpg', 'jpeg', 'png'])

        if uploaded_file is not None:
            try:
                # Display the uploaded image
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image', use_container_width=True)

                # Process image when analyze button is clicked
                if st.button('Analyze Image'):
                    with st.spinner('Analyzing image...'):
                        # Save the image
                        image_path = save_uploaded_image(uploaded_file)

                        # Process the image
                        processed_image = process_image(image)

                        # Get prediction
                        prediction, confidence = predict_disease(processed_image)

                        # Get treatment recommendations
                        recommendations = get_treatment_recommendations(prediction)
                        treatment_text = "\n".join(recommendations)

                        # Save to database
                        save_diagnosis(
                            disease=prediction,
                            confidence=confidence,
                            image_path=image_path,
                            treatment_plan=treatment_text
                        )

                        # Display results
                        st.subheader("Diagnosis Results")
                        st.write(f"Detected Issue: {prediction}")
                        st.write(f"Confidence: {confidence:.2f}%")

                        st.subheader("Treatment Recommendations")
                        for idx, rec in enumerate(recommendations, 1):
                            st.write(f"{idx}. {rec}")

                        st.info("Note: This is a preliminary diagnosis. For severe cases, please consult an agricultural expert.")

            except Exception as e:
                st.error(f"An error occurred while processing the image: {str(e)}")
                st.write("Please try uploading a different image or check if the image is corrupted.")

    with tab2:
        st.subheader("Recent Diagnoses")
        recent_records = get_recent_diagnoses()

        if recent_records:
            for record in recent_records:
                with st.expander(f"{record.disease} - {record.timestamp.strftime('%Y-%m-%d %H:%M')}"):
                    st.write(f"Confidence: {record.confidence:.2f}%")
                    if os.path.exists(record.image_path):
                        st.image(record.image_path, caption="Diagnosed Image", use_container_width=True)
                    st.write("Treatment Plan:")
                    st.write(record.treatment_plan)
        else:
            st.write("No diagnosis records found.")

if __name__ == "__main__":
    main()