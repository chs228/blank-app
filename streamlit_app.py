import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st
from skimage.feature import hog

# Function to extract HOG features from an image
def extract_hog_features(image):
    fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)
    return fd

# Function to train the SVM classifier
def train_svm(X_train, y_train):
    clf = SVC(kernel='linear', random_state=42)
    clf.fit(X_train, y_train)
    return clf

# Load your dataset (replace with your own image dataset)
# Example: list of images and labels
images = [cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE), cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)]
labels = [0, 1]  # 0 for non-object, 1 for object, adjust based on your dataset

# Extract HOG features from all images
features = [extract_hog_features(image) for image in images]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train the SVM classifier
clf = train_svm(X_train, y_train)

# Test the model
y_pred = clf.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

# Streamlit web app for image upload and detection
st.title("AI Object Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read and process the image
    image = np.array(cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1))
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    feature = extract_hog_features(image_gray)

    # Make prediction
    prediction = clf.predict([feature])
    
    st.image(image, caption='Uploaded Image', use_column_width=True)
    if prediction[0] == 1:
        st.write("Object Detected!")
    else:
        st.write("No Object Detected.")
