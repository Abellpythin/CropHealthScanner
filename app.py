import streamlit as st
import numpy as np
from PIL import Image
import io
from image_processor import process_image
from model_handler import predict_disease
from utils import get_treatment_recommendations

def main():
    st.title("Crop Disease Diagnosis Tool")

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
                    # Process the image
                    processed_image = process_image(image)

                    # Get prediction
                    prediction, confidence = predict_disease(processed_image)

                    # Display results
                    st.subheader("Diagnosis Results")
                    st.write(f"Detected Issue: {prediction}")
                    st.write(f"Confidence: {confidence:.2f}%")

                    # Get and display treatment recommendations
                    recommendations = get_treatment_recommendations(prediction)

                    st.subheader("Treatment Recommendations")
                    for idx, rec in enumerate(recommendations, 1):
                        st.write(f"{idx}. {rec}")

                    st.info("Note: This is a preliminary diagnosis. For severe cases, please consult an agricultural expert.")

        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")
            st.write("Please try uploading a different image or check if the image is corrupted.")

if __name__ == "__main__":
    main()