import torch

# Create an instance of MSELoss
criterion = torch.nn.MSELoss()

# Example predicted values
predicted = torch.tensor([1.2, 2.5, 3.8, 4.1])

# Example ground-truth values
target = torch.tensor([1.0, 2.0, 4.0, 4.5])

# Calculate the loss
loss = criterion(predicted, target)

print(f"MSE Loss: {loss:.4f}")
