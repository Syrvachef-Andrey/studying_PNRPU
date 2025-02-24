import random
import torch
import torch.nn.functional as F
from torchvision import datasets, transforms
import matplotlib.pyplot as plt


# Загрузка датасета MNIST
def load_dataset():
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    x_train = train_data.data.float() / 255.0
    x_train = x_train.view(-1, 784)
    y_train = torch.eye(10)[train_data.targets]
    return x_train, y_train


images, labels = load_dataset()

weights_input_to_hidden = torch.randn(20, 784, requires_grad=True)
weights_hidden_to_output = torch.randn(10, 20, requires_grad=True)
bias_input_to_hidden = torch.zeros(20, requires_grad=True)
bias_hidden_to_output = torch.zeros(10, requires_grad=True)

epochs = 15
learning_rate = 0.01

for epoch in range(epochs):
    print(f"Epoch №{epoch}")
    e_loss = 0
    e_correct = 0

    for image, label in zip(images, labels):
        image = image.unsqueeze(1)
        label = label.unsqueeze(1)

        hidden_raw = weights_input_to_hidden @ image + bias_input_to_hidden.unsqueeze(1)
        hidden = torch.sigmoid(hidden_raw)
        output_raw = weights_hidden_to_output @ hidden + bias_hidden_to_output.unsqueeze(1)
        output = torch.sigmoid(output_raw)

        loss = torch.mean((output - label) ** 2)
        e_loss += loss.item()
        e_correct += int(torch.argmax(output) == torch.argmax(label))

        loss.backward()

        with torch.no_grad():
            weights_input_to_hidden -= learning_rate * weights_input_to_hidden.grad
            weights_hidden_to_output -= learning_rate * weights_hidden_to_output.grad
            bias_input_to_hidden -= learning_rate * bias_input_to_hidden.grad
            bias_hidden_to_output -= learning_rate * bias_hidden_to_output.grad

            weights_input_to_hidden.grad.zero_()
            weights_hidden_to_output.grad.zero_()
            bias_input_to_hidden.grad.zero_()
            bias_hidden_to_output.grad.zero_()

    print(f"Loss: {round((e_loss / images.shape[0]) * 100, 3)}%")
    print(f"Accuracy: {round((e_correct / images.shape[0]) * 100, 3)}%")

# Сохранение весов
torch.save(weights_input_to_hidden, 'weights_input_to_hidden.pt')
torch.save(weights_hidden_to_output, 'weights_hidden_to_output.pt')
torch.save(bias_input_to_hidden, 'bias_input_to_hidden.pt')
torch.save(bias_hidden_to_output, 'bias_hidden_to_output.pt')

test_image = random.choice(images)
image = test_image.unsqueeze(1)

hidden_raw = weights_input_to_hidden @ image + bias_input_to_hidden.unsqueeze(1)
hidden = torch.sigmoid(hidden_raw)
output_raw = weights_hidden_to_output @ hidden + bias_hidden_to_output.unsqueeze(1)
output = torch.sigmoid(output_raw)

plt.imshow(test_image.view(28, 28), cmap="Greys")
plt.title(f"NN suggests the number is: {torch.argmax(output).item()}")
plt.show()