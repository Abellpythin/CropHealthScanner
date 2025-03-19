import streamlit as st
import numpy as np
from PIL import Image
import io
import qrcode
from image_processor import process_image
from model_handler import predict_disease
from utils import get_treatment_recommendations

def generate_qr_code(url):
    """Generate QR code for the given URL"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction
        box_size=12,  # Larger box size
        border=5,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    return qr_image

def main():
    st.title("Crop Disease Diagnosis Tool")

    # Add QR code in sidebar
    st.sidebar.title("Share Application")
    if st.sidebar.button("Generate QR Code"):
        # Use a direct app URL
        qr_image = generate_qr_code("https://crop-disease-diagnosis.replit.app")

        # Convert PIL image to bytes
        img_byte_arr = io.BytesIO()
        qr_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        st.sidebar.image(img_byte_arr, caption="Scan this QR code to access the app", use_container_width=True)
        st.sidebar.download_button(
            label="Download QR Code",
            data=img_byte_arr,
            file_name="crop_diagnosis_app_qr.png",
            mime="image/png"
        )

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