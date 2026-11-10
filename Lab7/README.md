# Lab 7: Explainable AI, Adversarial AI, PCA and SVD

## Aim
To understand Explainable AI, Adversarial AI, dimensionality reduction, and matrix decomposition using Python.

## Problem Statement
Implement a CNN-based image classification mini-project and demonstrate Grad-CAM, FGSM, PCA, and SVD techniques.

## Tools and Libraries
- Python
- PyTorch
- NumPy
- Matplotlib
- Pillow

## Experiments Performed

### 1. CNN Image Classification
Created a dataset of circles and squares and trained a Convolutional Neural Network to classify the images.

### 2. Grad-CAM
Generated a heatmap to identify image regions that influence the CNN's prediction.

### 3. FGSM
Applied the Fast Gradient Sign Method to generate an adversarial image using input gradients.

### 4. PCA
Reduced image features from 1024 dimensions to 2 principal components for visualization.

### 5. SVD
Performed Singular Value Decomposition and reconstructed an image using the first five singular values.

## Results
- Trained a CNN for shape classification.
- Generated Grad-CAM heatmap visualizations.
- Applied an FGSM adversarial perturbation.
- Reduced image dimensions using PCA.
- Reconstructed an image using SVD.

## Output Files
- `training_loss.png`
- `gradcam_visualization.png`
- `fgsm_attack.png`
- `pca_visualization.png`
- `svd_visualization.png`
- `training_output.png`

## Learning Outcomes
- Understood CNN-based image classification.
- Learned the importance of Explainable AI.
- Understood Grad-CAM visualization.
- Learned how adversarial attacks work using FGSM.
- Understood dimensionality reduction using PCA.
- Learned matrix decomposition using SVD.

## Conclusion
The experiment demonstrated image classification using CNNs and explored model explainability, adversarial attacks, dimensionality reduction, and image reconstruction.