
import os
import random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw
from torch.utils.data import Dataset, DataLoader

# Create folders
os.makedirs("Lab7/outputs", exist_ok=True)

# Set random seeds
torch.manual_seed(42)
np.random.seed(42)
random.seed(42)

# ==========================================
# EXPERIMENT 1: CREATE IMAGE DATASET
# ==========================================

print("EXPERIMENT 1: IMAGE DATASET")

class ShapeDataset(Dataset):

    def __init__(self, size):
        self.size = size

    def __len__(self):
        return self.size

    def __getitem__(self, index):

        rng = random.Random(index)

        # 0 = Circle, 1 = Square
        label = index % 2

        image = Image.new("L", (32, 32), 0)
        draw = ImageDraw.Draw(image)

        x = rng.randint(8, 16)
        y = rng.randint(8, 16)
        shape_size = rng.randint(7, 12)

        if label == 0:
            draw.ellipse(
                (x, y, x + shape_size, y + shape_size),
                fill=255
            )
        else:
            draw.rectangle(
                (x, y, x + shape_size, y + shape_size),
                fill=255
            )

        image_array = np.array(image, dtype=np.float32) / 255.0

        tensor = torch.tensor(image_array).unsqueeze(0)

        return tensor, label


train_dataset = ShapeDataset(160)
test_dataset = ShapeDataset(40)

train_loader = DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=16
)

print("Training images:", len(train_dataset))
print("Testing images:", len(test_dataset))


# ==========================================
# EXPERIMENT 2: CNN MODEL TRAINING
# ==========================================

print("\nEXPERIMENT 2: CNN MODEL TRAINING")


class CNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(1, 8, 3, padding=1)
        self.conv2 = nn.Conv2d(8, 16, 3, padding=1)

        self.pool = nn.MaxPool2d(2, 2)

        self.fc1 = nn.Linear(16 * 8 * 8, 32)
        self.fc2 = nn.Linear(32, 2)

        self.feature_maps = None

    def forward(self, x):

        x = self.pool(F.relu(self.conv1(x)))

        x = F.relu(self.conv2(x))

        # Save feature maps for Grad-CAM
        self.feature_maps = x

        if x.requires_grad:
            x.retain_grad()

        x = self.pool(x)

        x = x.reshape(x.size(0), -1)

        x = F.relu(self.fc1(x))

        return self.fc2(x)


model = CNN()

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

loss_values = []

# Training
for epoch in range(10):

    model.train()

    total_loss = 0

    for images, labels in train_loader:

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(train_loader)

    loss_values.append(average_loss)

    print(
        "Epoch:", epoch + 1,
        "Loss:", round(average_loss, 4)
    )


# Test model accuracy
model.eval()

correct = 0
total = 0

with torch.no_grad():

    for images, labels in test_loader:

        outputs = model(images)

        predictions = outputs.argmax(dim=1)

        correct += (predictions == labels).sum().item()

        total += labels.size(0)

accuracy = 100 * correct / total

print("Test Accuracy:", round(accuracy, 2), "%")

# Save training loss graph
plt.figure(figsize=(7, 5))

plt.plot(loss_values)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("CNN Training Loss")

plt.savefig("Lab7/outputs/training_loss.png")
plt.close()


# ==========================================
# EXPERIMENT 3: GRAD-CAM
# ==========================================

print("\nEXPERIMENT 3: GRAD-CAM")

model.eval()

image, actual_label = test_dataset[0]

input_image = image.unsqueeze(0)

model.zero_grad()

output = model(input_image)

predicted_class = output.argmax(dim=1).item()

# Calculate gradients
score = output[0, predicted_class]

score.backward()

# Get feature maps and gradients
features = model.feature_maps.detach()

gradients = model.feature_maps.grad.detach()

# Calculate importance weights
weights = gradients.mean(dim=(2, 3), keepdim=True)

# Generate Grad-CAM heatmap
cam = (weights * features).sum(dim=1, keepdim=True)

cam = F.relu(cam)

cam = F.interpolate(
    cam,
    size=(32, 32),
    mode="bilinear",
    align_corners=False
)

cam = cam.squeeze().numpy()

cam = cam / (cam.max() + 1e-8)

# Display Grad-CAM
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(image.squeeze(), cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cam, cmap="jet")
plt.title("Grad-CAM Heatmap")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(image.squeeze(), cmap="gray")
plt.imshow(cam, cmap="jet", alpha=0.5)
plt.title("Grad-CAM Overlay")
plt.axis("off")

plt.tight_layout()

plt.savefig("Lab7/outputs/gradcam_visualization.png")
plt.close()

print("Actual Class:", actual_label)
print("Predicted Class:", predicted_class)
print("Grad-CAM visualization saved.")


# ==========================================
# EXPERIMENT 4: FGSM ATTACK
# ==========================================

print("\nEXPERIMENT 4: FGSM ATTACK")

model.eval()

image, label = test_dataset[1]

input_image = image.unsqueeze(0).clone().detach()
input_image.requires_grad = True

model.zero_grad()

output = model(input_image)

original_prediction = output.argmax(dim=1).item()

loss = criterion(
    output,
    torch.tensor([label])
)

loss.backward()

# FGSM perturbation
epsilon = 0.15

perturbed_image = (
    input_image + epsilon * input_image.grad.sign()
).detach()

perturbed_image = torch.clamp(
    perturbed_image,
    0,
    1
)

# Predict after attack
with torch.no_grad():

    attacked_output = model(perturbed_image)

    attacked_prediction = attacked_output.argmax(dim=1).item()

print("Actual Class:", label)
print("Original Prediction:", original_prediction)
print("Prediction After FGSM:", attacked_prediction)

# Display FGSM results
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(image.squeeze(), cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(perturbed_image.squeeze(), cmap="gray")
plt.title("FGSM Image")
plt.axis("off")

plt.subplot(1, 3, 3)
difference = (
    perturbed_image - input_image.detach()
).abs().squeeze()

plt.imshow(difference, cmap="hot")
plt.title("Perturbation")
plt.axis("off")

plt.tight_layout()

plt.savefig("Lab7/outputs/fgsm_attack.png")
plt.close()

print("FGSM visualization saved.")


# ==========================================
# EXPERIMENT 5: PCA
# ==========================================

print("\nEXPERIMENT 5: PRINCIPAL COMPONENT ANALYSIS")

# Convert images into feature vectors
all_images = []

all_labels = []

for i in range(200):

    image, label = (
        train_dataset[i]
        if i < 160
        else test_dataset[i - 160]
    )

    all_images.append(image.numpy().flatten())

    all_labels.append(label)

data = np.array(all_images)

# Mean center the data
mean = np.mean(data, axis=0)

centered_data = data - mean

# Perform SVD to calculate PCA components
U, S, Vt = np.linalg.svd(
    centered_data,
    full_matrices=False
)

# Project data onto first two components
pca_result = centered_data @ Vt[:2].T

plt.figure(figsize=(7, 5))

for label, name in [(0, "Circle"), (1, "Square")]:

    selected = np.array(all_labels) == label

    plt.scatter(
        pca_result[selected, 0],
        pca_result[selected, 1],
        label=name
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization")
plt.legend()

plt.savefig("Lab7/outputs/pca_visualization.png")
plt.close()

print("Original Features:", data.shape[1])
print("Reduced Features:", pca_result.shape[1])
print("PCA visualization saved.")


# ==========================================
# EXPERIMENT 6: SVD
# ==========================================

print("\nEXPERIMENT 6: SINGULAR VALUE DECOMPOSITION")

# Decompose a sample image matrix
sample_image = data[0].reshape(32, 32)

U_img, S_img, Vt_img = np.linalg.svd(
    sample_image,
    full_matrices=False
)

# Reconstruct image using first 5 singular values
k = 5

reconstructed = (
    U_img[:, :k]
    @ np.diag(S_img[:k])
    @ Vt_img[:k, :]
)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(sample_image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(reconstructed, cmap="gray")
plt.title("SVD Reconstruction (5 Components)")
plt.axis("off")

plt.tight_layout()

plt.savefig("Lab7/outputs/svd_visualization.png")
plt.close()

print("Number of Singular Values:", len(S_img))
print("SVD reconstruction saved.")


# ==========================================
# FINAL RESULT
# ==========================================

print("\nALL EXPERIMENTS COMPLETED SUCCESSFULLY!")
print("LAB 7 COMPLETED.")

