import torch

# Create an instance of MSELoss
criterion = torch.nn.MSELoss()

predicted = torch.tensor([1.2]) # Predicted values
target    = torch.tensor([1.0]) # Ground-truth (i. e. target) values

# Calculate the loss
loss = criterion(predicted, target)

print(f"MSE Loss: {loss:.4f}")
