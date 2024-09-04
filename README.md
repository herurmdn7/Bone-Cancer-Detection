
# Bone Cancer Detection

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Installation and Setup](#installation-and-setup)
4. [Data](#data)
5. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6. [Modeling Approach](#modeling-approach)
7. [Results](#results)
8. [Conclusion](#conclusion)
9. [Future Work](#future-work)
10. [References](#references)

---

### 1. Project Overview
This project aims to detect bone cancer using machine learning models trained on image data. The model is designed to classify bone images into cancerous and non-cancerous categories, helping in early detection and treatment.

---

### 2. Project Structure
```bash
├── P2G7_Heru.ipynb              # Jupyter notebook for data processing, model training, and evaluation
├── P2G7_Heru_inference.ipynb    # Notebook for performing inference on test data
├── README.md                    # Project README file
├── model_adam2.keras            # Saved model after improvement
```

---

### 3. Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/herurmdn7/Bone-Cancer-Detection.git
   ```
2. Ensure Python (version >=3.7) and Jupyter Notebook are installed.

---

### 4. Data
- **Source**: The dataset is sourced from [Roboflow Bone Cancer Detection Dataset](https://universe.roboflow.com/normal-bones/bone-cancer-detection-xa7ru), containing bone cancer and normal bone images.
- **Class Distribution**:
  - **Training Set**: 7,057 images (3,081 cancerous, 3,976 normal)
  - **Test Set**: 872 images (384 cancerous, 488 normal)
- **Preprocessing**: The images were resized, normalized, and split into training and test sets. Data augmentation techniques were applied to improve model performance.

---

### 5. Exploratory Data Analysis (EDA)
- The class distribution was analyzed for both training and test sets to ensure balanced data for model training.
- Visualization of a few samples of cancerous and non-cancerous images helped to understand the complexity of the classification task.

---

### 6. Modeling Approach
- **Initial Model**: A basic Convolutional Neural Network (CNN) was built using Keras Sequential API.
- **Model Improvements**:
  - An improved model with additional layers and early stopping was trained to reduce overfitting and enhance recall.
  - **Optimizer**: Adam optimizer was used with fine-tuned learning rates.
  - The model was trained on augmented data to improve generalization.
- **Model Evaluation**: The model was evaluated on the test set using metrics such as loss, recall, precision, and F1-score.

---

### 7. Results
- The final model achieved a high recall on the test set with 91% score, indicating effective cancer detection.

---

### 8. Conclusion
The model showed strong performance in detecting bone cancer with a high recall rate, making it useful for early detection. However, there is room for improvement in reducing the loss.

---

### 9. Future Work
- **Model Enhancement**: Explore deeper architectures like ResNet or EfficientNet to improve accuracy and reduce overfitting.
- **Transfer Learning**: Use pre-trained models to improve generalization on smaller datasets.
- **Deployment**: The model is deployed for real-time detection on [Hugging Face Space](https://huggingface.co/spaces/Flickerjet/Bone_Cancer_Prediction).

---

### 10. References
- Tools: Python, TensorFlow, Keras, Roboflow
- Dataset: [Roboflow Bone Cancer Detection Dataset](https://universe.roboflow.com/normal-bones/bone-cancer-detection-xa7ru)
- Model File: [Download Model](https://drive.google.com/file/d/1YkEe2rZVwIMvLz0qa9lWHlBJnPxh6QIU/view?usp=sharing)
- Deployment: [Hugging Face Space](https://huggingface.co/spaces/Flickerjet/Bone_Cancer_Prediction)
