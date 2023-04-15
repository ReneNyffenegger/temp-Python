import matplotlib.pyplot as plt
import torch
from   torchvision import datasets
from   torchvision.transforms import ToTensor

training_data = datasets.FashionMNIST(
    root      ='data',                    # name of local directory to store downloaded data
    train     = True,
    download  = True,
    transform = ToTensor()
)


labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

#
# figsize is the size of the entire image.
#
figure = plt.figure(figsize = (4.9, 7.8))
print(type(figure)) # class 'matplotlib.figure.Figure'

cols, rows = 4, 5

for i in range(cols * rows):

    rndIx = torch.randint(len(training_data), size=(1,)).item()

    img, label = training_data[rndIx]
    figure.add_subplot(rows, cols, i+1)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap='gray')

plt.show()
