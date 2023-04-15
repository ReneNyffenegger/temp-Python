import torch
import torch.nn as nn

# Create a dummy model output and target
output = torch.tensor([[0.1, 0.2, 0.7], [0.8, 0.1, 0.1]])
target = torch.tensor([2, 0])

# Instantiate the criterion (CrossEntropyLoss in this case)
criterion = nn.CrossEntropyLoss()

# Calculate the loss
loss = criterion(output, target)
print("Loss:", loss.item())
