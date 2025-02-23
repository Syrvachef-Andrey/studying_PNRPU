import random
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

import utils_for_the_first_neuronetwork

# Загрузка данных
images, labels = utils_for_the_first_neuronetwork.load_dataset()

# Преобразуем данные в тензоры PyTorch
images = torch.tensor(images, dtype=torch.float32)
labels = torch.tensor(labels, dtype=torch.float32)

# Инициализация весов и смещений
weights_input_to_hidden = torch.rand((20, 784), requires_grad=True) * 2 - 1  # равномерное распределение от -0.5 до 0.5
weights_hidden_to_output = torch.rand((10, 20), requires_grad=True) * 2 - 1

bias_input_to_hidden = torch.zeros((20, 1), requires_grad=True)
bias_hidden_to_output = torch.zeros((10, 1), requires_grad=True)

# Гиперпараметры
epochs = 5
learning_rate = 0.01

# Цикл обучения
for epoch in range(epochs):
    print(f"Epoch №{epoch}")

    e_loss = 0
    e_correct = 0

    for image, label in zip(images, labels):
        image = image.view(-1, 1)
        label = label.view(-1, 1)

        # Forward propagation
        hidden_raw = weights_input_to_hidden @ image + bias_input_to_hidden
        hidden = torch.sigmoid(hidden_raw)

        output_raw = weights_hidden_to_output @ hidden + bias_hidden_to_output
        output = torch.sigmoid(output_raw)

        # Вычисление потерь и точности
        loss = F.mse_loss(output, label)
        e_loss += loss.item()
        e_correct += int(torch.argmax(output) == torch.argmax(label))

        # Backpropagation
        loss.backward()

        # Обновление весов и смещений
        with torch.no_grad():
            weights_hidden_to_output -= learning_rate * weights_hidden_to_output.grad
            bias_hidden_to_output -= learning_rate * bias_hidden_to_output.grad

            weights_input_to_hidden -= learning_rate * weights_input_to_hidden.grad
            bias_input_to_hidden -= learning_rate * bias_input_to_hidden.grad

            # Обнуляем градиенты
            weights_hidden_to_output.grad.zero_()
            bias_hidden_to_output.grad.zero_()
            weights_input_to_hidden.grad.zero_()
            bias_input_to_hidden.grad.zero_()

    print(f"Loss: {round((e_loss / images.shape[0]) * 100, 3)}%")
    print(f"Accuracy: {round((e_correct / images.shape[0]) * 100, 3)}%")

# Сохранение весов и смещений с помощью PyTorch
torch.save(weights_input_to_hidden, 'weights_input_to_hidden.pth')
torch.save(weights_hidden_to_output, 'weights_hidden_to_output.pth')
torch.save(bias_input_to_hidden, 'bias_input_to_hidden.pth')
torch.save(bias_hidden_to_output, 'bias_hidden_to_output.pth')

# Тестирование модели
test_image = random.choice(images)

image = test_image.view(-1, 1)

hidden_raw = weights_input_to_hidden @ image + bias_input_to_hidden
hidden = torch.sigmoid(hidden_raw)

output_raw = weights_hidden_to_output @ hidden + bias_hidden_to_output
output = torch.sigmoid(output_raw)

plt.imshow(test_image.view(28, 28), cmap="Greys")
plt.title(f"NN suggests the number is: {output.argmax().item()}")
plt.show()