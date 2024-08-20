import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Load the model
def run():
    # File uploader for image input
    file = st.file_uploader("Upload an image", type=["jpg", "png"])

    # Load the pre-trained model
    model = load_model('model_adam-4.keras')
    img_height, img_width = 225, 225  # Define the target size for the image

    # Function to preprocess the image and make a prediction
    def import_and_predict(image_data, model):
        # Load and preprocess the image
        image = load_img(image_data, target_size=(img_height, img_width))
        img_array = img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to create a batch
        img_array = img_array / 255.0  # Normalize the image

        # Make prediction
        predictions = model.predict(img_array)

        # Determine the class based on prediction threshold
        result_pred = np.where(predictions < 0.1, 0, 1).item()

        # Define class labels
        class_labels = ['Cancer', 'Normal']
        result = f"Prediction: {class_labels[result_pred]}"

        return result

    # Display image and prediction result
    if file is None:
        st.text("Please upload an image file")
    else:
        result = import_and_predict(file, model)
        st.image(file)
        st.write(result)

if __name__ == "__main__":
    run()
