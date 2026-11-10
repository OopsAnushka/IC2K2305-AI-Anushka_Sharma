
import os
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Create folders
os.makedirs("Lab6/outputs", exist_ok=True)
os.makedirs("models", exist_ok=True)

torch.manual_seed(42)

# ==========================================
# EXPERIMENT 1: PYTORCH TENSOR OPERATIONS
# ==========================================

print("EXPERIMENT 1: TENSOR OPERATIONS")

a = torch.tensor([1, 2, 3, 4])
b = torch.tensor([5, 6, 7, 8])

print("Tensor A:", a)
print("Tensor B:", b)
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Mean of A:", a.float().mean())

# ==========================================
# EXPERIMENT 2: AUTOGRAD
# ==========================================

print("\nEXPERIMENT 2: AUTOGRAD")

x = torch.tensor(2.0, requires_grad=True)

y = x ** 2

y.backward()

print("Value of x:", x.item())
print("Value of y:", y.item())
print("Gradient:", x.grad.item())

# ==========================================
# EXPERIMENT 3: LINEAR REGRESSION
# ==========================================

print("\nEXPERIMENT 3: LINEAR REGRESSION")

# Generate sample data: y = 3x + 2
X = torch.linspace(0, 10, 100).reshape(-1, 1)
Y = 3 * X + 2 + torch.randn(100, 1) * 0.5

# Create linear regression model
linear_model = nn.Linear(1, 1)

# Loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(
    linear_model.parameters(),
    lr=0.01
)

loss_values = []

# Training loop
for epoch in range(500):

    predictions = linear_model(X)

    loss = criterion(predictions, Y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    loss_values.append(loss.item())

print("Final Loss:", round(loss.item(), 4))

weight = linear_model.weight.item()
bias = linear_model.bias.item()

print("Learned Weight:", round(weight, 2))
print("Learned Bias:", round(bias, 2))

# Save linear regression model
torch.save(
    linear_model.state_dict(),
    "models/linear_regression.pth"
)

# Plot linear regression
plt.figure(figsize=(8, 5))

plt.scatter(X.numpy(), Y.numpy(), label="Actual Data")
plt.plot(
    X.numpy(),
    linear_model(X).detach().numpy(),
    label="Predicted Line"
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression using PyTorch")
plt.legend()
plt.savefig("Lab6/outputs/linear_regression.png")
plt.show()

# ==========================================
# EXPERIMENT 4: NEURAL NETWORK (XOR)
# ==========================================

print("\nEXPERIMENT 4: NEURAL NETWORK")

# XOR dataset
inputs = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

targets = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])

# Create neural network
neural_model = nn.Sequential(
    nn.Linear(2, 8),
    nn.Tanh(),
    nn.Linear(8, 1)
)

loss_function = nn.BCEWithLogitsLoss()

optimizer = torch.optim.Adam(
    neural_model.parameters(),
    lr=0.05
)

nn_losses = []

# Train neural network
for epoch in range(2000):

    output = neural_model(inputs)

    loss = loss_function(output, targets)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    nn_losses.append(loss.item())

# Make predictions
with torch.no_grad():
    predictions = torch.sigmoid(
        neural_model(inputs)
    )

predicted_classes = (predictions >= 0.5).int()

print("Actual XOR Output:", targets.int().flatten().tolist())
print("Predicted Output:", predicted_classes.flatten().tolist())

# Save neural network model
torch.save(
    neural_model.state_dict(),
    "models/xor_neural_network.pth"
)

# Plot neural network training loss
plt.figure(figsize=(8, 5))

plt.plot(nn_losses)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Neural Network Training Loss")
plt.savefig("Lab6/outputs/neural_network_loss.png")
plt.show()

# ==========================================
# FINAL RESULT
# ==========================================

print("\nAll experiments completed successfully!")
print("Models and graphs saved successfully.")
print("LAB 6 COMPLETED.")

