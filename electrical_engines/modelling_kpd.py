import numpy as np
import matplotlib.pyplot as plt

# Номинальный КПД (берем из справочника для нашего типа передачи)
eta_n = 0.92  # Номинальный КПД (при K3 = 1)

# Создаем массив коэффициентов загрузки от 0 до 1.25
K3 = np.linspace(0, 1.25, 100)

# Функция для расчета КПД привода по формуле
def calculate_efficiency(K, eta_nom):
    """
    Расчет КПД привода в зависимости от коэффициента загрузки.
    """
    numerator = K * eta_nom

    term1 = 0.6 * (1 - eta_nom)       # Постоянные потери
    term2 = 0.6 * K * eta_nom         # Переменные потери, зависящие от нагрузки
    term3 = 0.4 * K                   # Еще одна составляющая переменных потерь

    denominator = term1 + term2 + term3

    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.where(K != 0, numerator / denominator, 0)

    return result

# Рассчитываем значения КПД для всех K3
eta_p = calculate_efficiency(K3, eta_n)

# Находим значение при номинале (K3=1) для проверки
eta_at_nominal = calculate_efficiency(1.0, eta_n)
print(f"Проверка: при K3 = 1, eta_п = {eta_at_nominal:.4f} (должно быть {eta_n})")

# Построение графика
plt.figure(figsize=(10, 6))

plt.plot(K3, eta_p * 100, 'b-', linewidth=2, label='КПД привода')  # Умножаем на 100 для процентов
plt.axhline(y=eta_n * 100, color='r', linestyle='--', linewidth=1, label=f'Номинальный КПД ({eta_n*100:.1f}%)')
plt.axvline(x=1.0, color='gray', linestyle=':', linewidth=1, label='K₃ = 1 (номинал)')

plt.plot(1.0, eta_n * 100, 'ro', markersize=8)

plt.xlabel('Коэффициент загрузки K₃')
plt.ylabel('КПД привода, %')
plt.title('Зависимость КПД механической передачи от коэффициента загрузки')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.ylim(0, 100)
plt.xlim(0, 1.25)

plt.tight_layout()
plt.show()
