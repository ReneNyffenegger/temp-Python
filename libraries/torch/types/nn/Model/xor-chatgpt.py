import torch
import torch.nn as nn
import torch.optim as optim

# Input values
X = torch.tensor([
      [0, 0],
      [0, 1],
      [1, 0],
      [1, 1]
  ],
  dtype=torch.float32)

# Expected output values
Y = torch.tensor([
      [0],
      [1],
      [1],
      [0]
    ],
    dtype=torch.float32)


# Define the neural network model

class XORModel(nn.Module):

    def __init__(self):
#       super(XORModel, self).__init__()
        super().__init__()
        self.layer1 = nn.Linear(2, 2)
        self.layer2 = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.sigmoid(self.layer1(x))
        x = torch.sigmoid(self.layer2(x))
        return x

# Initialize the model, loss function, and optimizer
model     = XORModel()
criterion = nn.MSELoss() #  Mean squared error loss
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Train the model
num_epochs = 50000
for epoch in range(num_epochs):

  # Forward pass
    outputs = model(X)
    loss    = criterion(outputs, Y)

  # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

  # Print progress
    if (epoch + 1) % 1000 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# Test the model
with torch.no_grad():

    test_outputs = model(X)
    predicted = (test_outputs > 0.5).float()
    accuracy  = (predicted == Y).float().mean()

    print(f'Accuracy: {accuracy:.2f}')
