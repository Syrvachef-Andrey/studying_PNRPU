import torch
from torch import nn, optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

trainset = torchvision.datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)
testset = torchvision.datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)

trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
testloader = DataLoader(testset, batch_size=64, shuffle=False)

# === ВИЗУАЛИЗАЦИЯ ДАННЫХ ===

# Список названий классов для Fashion-MNIST
class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]


def show_dataset_info(trainset, testset):
    """Выводит основную информацию о датасете"""
    print("📊 ИНФОРМАЦИЯ О ДАТАСЕТЕ:")
    print(f"Размер тренировочного набора: {len(trainset)} изображений")
    print(f"Размер тестового набора: {len(testset)} изображений")
    print(f"Размер изображений: {trainset[0][0].shape}")
    print(f"Количество классов: {len(class_names)}")
    print("Классы:", class_names)
    print("-" * 50)


def show_sample_images(dataset, class_names, num_images=12):
    """
    Показывает случайные изображения из датасета
    """
    # Выбираем случайные индексы
    indices = np.random.choice(len(dataset), num_images, replace=False)

    # Создаем сетку для отображения
    fig, axes = plt.subplots(3, 4, figsize=(15, 12))
    axes = axes.ravel()

    for i, idx in enumerate(indices):
        # Получаем изображение и метку
        image, label = dataset[idx]

        # Денормализуем изображение для корректного отображения
        image = image * 0.5 + 0.5  # обратное преобразование нормализации
        image = image.squeeze()  # убираем dimension канала (1,28,28) -> (28,28)

        # Отображаем изображение
        axes[i].imshow(image, cmap='gray')
        axes[i].set_title(f'{label}: {class_names[label]}', fontsize=12, pad=10)
        axes[i].axis('off')

    plt.suptitle('Случайные изображения из Fashion-MNIST', fontsize=16, y=0.95)
    plt.tight_layout()
    plt.show()


def show_batch_images(dataloader, class_names, num_images=8):
    """
    Показывает изображения из первого батча DataLoader
    """
    # Получаем первый батч
    dataiter = iter(dataloader)
    images, labels = next(dataiter)

    print(f"Размер батча: {images.shape}")  # [batch_size, channels, height, width]
    print(f"Диапазон значений пикселей: [{images.min():.3f}, {images.max():.3f}]")

    # Создаем сетку для отображения
    fig, axes = plt.subplots(2, 4, figsize=(15, 8))
    axes = axes.ravel()

    for i in range(min(num_images, len(images))):
        # Подготавливаем изображение
        img = images[i]
        img = img * 0.5 + 0.5  # денормализация
        img = img.squeeze()  # убираем dimension канала

        # Отображаем
        axes[i].imshow(img, cmap='gray')
        axes[i].set_title(f'Метка: {labels[i].item()} - {class_names[labels[i]]}',
                          fontsize=12, pad=10)
        axes[i].axis('off')

    plt.suptitle(f'Изображения из первого батча (batch_size={len(images)})',
                 fontsize=16, y=0.95)
    plt.tight_layout()
    plt.show()


def show_class_distribution(dataset, class_names):
    """
    Показывает распределение классов в датасете
    """
    # Собираем все метки
    labels = [dataset[i][1] for i in range(len(dataset))]

    # Считаем количество каждого класса
    unique, counts = np.unique(labels, return_counts=True)

    # Создаем график
    plt.figure(figsize=(12, 6))
    bars = plt.bar(unique, counts, color='skyblue', edgecolor='black', alpha=0.7)

    # Добавляем подписи
    plt.xlabel('Классы')
    plt.ylabel('Количество изображений')
    plt.title('Распределение классов в датасете', fontsize=16)
    plt.xticks(unique, [class_names[i] for i in unique], rotation=45, ha='right')

    # Добавляем числа на столбцы
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
                 f'{count}', ha='center', va='bottom', fontweight='bold')

    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Выводим статистику
    print("\n📈 СТАТИСТИКА РАСПРЕДЕЛЕНИЯ КЛАССОВ:")
    for i, (cls, count) in enumerate(zip(unique, counts)):
        percentage = (count / len(dataset)) * 100
        print(f"{class_names[cls]:15}: {count:5} изображений ({percentage:5.1f}%)")


def show_image_statistics(dataset):
    """
    Показывает статистику пикселей изображений
    """
    # Собираем статистику по пикселям
    pixels = []
    for i in range(min(1000, len(dataset))):  # берем подмножество для скорости
        image, _ = dataset[i]
        pixels.extend(image.flatten().numpy())

    pixels = np.array(pixels)

    # Создаем гистограмму
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(pixels, bins=50, alpha=0.7, color='lightcoral', edgecolor='black')
    plt.xlabel('Значение пикселя')
    plt.ylabel('Частота')
    plt.title('Распределение значений пикселей')
    plt.grid(alpha=0.3)

    plt.subplot(1, 2, 2)
    # Показываем несколько изображений в разных стилях
    fig, axes = plt.subplots(2, 3, figsize=(10, 7))
    styles = ['gray', 'viridis', 'plasma', 'inferno', 'magma', 'cividis']

    for i, style in enumerate(styles):
        img, label = dataset[i]
        img = img.squeeze()
        row, col = i // 3, i % 3
        axes[row, col].imshow(img, cmap=style)
        axes[row, col].set_title(f'cmap: {style}')
        axes[row, col].axis('off')

    plt.suptitle('Разные цветовые схемы отображения', fontsize=14)
    plt.tight_layout()
    plt.show()

    print("\n📊 СТАТИСТИКА ПИКСЕЛЕЙ:")
    print(f"Минимальное значение: {pixels.min():.3f}")
    print(f"Максимальное значение: {pixels.max():.3f}")
    print(f"Среднее значение: {pixels.mean():.3f}")
    print(f"Стандартное отклонение: {pixels.std():.3f}")


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

model = NeuralNetwork().to(device)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)


# === ЭТАП 3: ЦИКЛ ОБУЧЕНИЯ ===

def train_one_epoch(model, trainloader, loss_fn, optimizer, device, print_every=200):
    """
    Функция для обучения модели на одной эпохе

    Args:
        model: нейронная сеть
        trainloader: DataLoader с тренировочными данными
        loss_fn: функция потерь
        optimizer: оптимизатор
        device: устройство (cpu/cuda)
        print_every: частота вывода логов (в батчах)
    """
    # Устанавливаем модель в режим обучения
    model.train()

    # Переменные для отслеживания прогресса
    running_loss = 0.0
    total_batches = len(trainloader)

    print(f"Начало эпохи. Всего батчей: {total_batches}")
    print("-" * 50)

    # Цикл по всем батчам в даталоадере
    for batch_idx, (data, targets) in enumerate(trainloader):
        # Перемещаем данные на нужное устройство (GPU/CPU)
        data = data.to(device)
        targets = targets.to(device)

        # 1. Обнуляем градиенты оптимизатора
        optimizer.zero_grad()

        # 2. Прямой проход (forward pass): вычисляем предсказания
        outputs = model(data)

        # 3. Вычисляем значение функции потерь
        loss = loss_fn(outputs, targets)

        # 4. Обратный проход (backward pass): вычисляем градиенты
        loss.backward()

        # 5. Шаг оптимизатора: обновляем веса
        optimizer.step()

        # Собираем статистику
        running_loss += loss.item()

        # Логирование каждые print_every батчей
        if (batch_idx + 1) % print_every == 0:
            avg_loss = running_loss / print_every
            current_batch = batch_idx + 1
            progress = (current_batch / total_batches) * 100

            print(f'Батч [{current_batch:4d}/{total_batches}], '
                  f'Прогресс: {progress:5.1f}%, '
                  f'Средние потери: {avg_loss:.4f}')

            # Сбрасываем running_loss для следующего интервала
            running_loss = 0.0

    # Выводим финальную статистику эпохи
    if total_batches % print_every != 0:
        remaining_batches = total_batches % print_every
        if remaining_batches > 0:
            avg_loss = running_loss / remaining_batches
            print(f'Финальные [{total_batches:4d}/{total_batches}], '
                  f'Средние потери: {avg_loss:.4f}')


# Дополнительная функция для вычисления точности на тренировочном наборе
def calculate_accuracy(model, dataloader, device):
    """
    Вычисляет точность модели на данном DataLoader
    """
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for data, targets in dataloader:
            data, targets = data.to(device), targets.to(device)
            outputs = model(data)
            _, predicted = torch.max(outputs.data, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()

    accuracy = 100 * correct / total
    return accuracy


# === ЗАПУСК ВИЗУАЛИЗАЦИИ И ОБУЧЕНИЯ ===
if __name__ == "__main__":
    # Визуализация данных
    print("🔍 ВИЗУАЛИЗАЦИЯ ДАННЫХ")
    print("=" * 60)

    # 1. Информация о датасете
    show_dataset_info(trainset, testset)

    # 2. Случайные изображения из тренировочного набора
    print("\n🖼️ СЛУЧАЙНЫЕ ИЗОБРАЖЕНИЯ ИЗ ТРЕНИРОВОЧНОГО НАБОРА:")
    show_sample_images(trainset, class_names)

    # 3. Изображения из первого батча
    print("\n📦 ИЗОБРАЖЕНИЯ ИЗ ПЕРВОГО БАТЧА:")
    show_batch_images(trainloader, class_names)

    # 4. Распределение классов
    print("\n📊 РАСПРЕДЕЛЕНИЕ КЛАССОВ В ТРЕНИРОВОЧНОМ НАБОРЕ:")
    show_class_distribution(trainset, class_names)

    # 5. Статистика пикселей
    print("\n🎨 СТАТИСТИКА ИЗОБРАЖЕНИЙ:")
    show_image_statistics(trainset)

    # Обучение модели
    print("\n" + "=" * 60)
    print("🚀 ЗАПУСК ОБУЧЕНИЯ МОДЕЛИ")
    print("=" * 60)

    # Обучаем на одной эпохе
    train_one_epoch(model, trainloader, loss_fn, optimizer, device, print_every=100)

    # Вычисляем точность после эпохи
    train_accuracy = calculate_accuracy(model, trainloader, device)
    print(f"\n✅ Точность на тренировочном наборе после эпохи: {train_accuracy:.2f}%")

    # Сохраняем модель после обучения
    torch.save(model.state_dict(), 'model_after_one_epoch.pth')
    print("💾 Модель сохранена как 'model_after_one_epoch.pth'")