import numpy as np
import matplotlib.pyplot as plt


def linear_regression_analysis():
    """
    Анализ линейной регрессии по 10 точкам данных - СТРОГАЯ СТРУКТУРА
    """
    print("=" * 80)
    print("АНАЛИЗ ЛИНЕЙНОЙ РЕГРЕССИИ - ПО МЕТОДИКЕ ИЗ ЛЕКЦИИ")
    print("=" * 80)

    # 1. Ввод данных ЭКС СПЕРМА ТОЧКИ
    print("\n1. ВХОДНЫЕ ДАННЫЕ")
    print("-" * 80)

    X = np.array([1, 2, 2, 3, 3, 4, 4, 4, 5, 6], dtype=float)
    Y = np.array([1, 1, 2, 3, 4, 3, 4, 5, 4, 4], dtype=float)

    n = len(X)
    print(f"X = {X}")
    print(f"Y = {Y}")
    print(f"n = {n} (количество экспериментальных точек)")

    # 2. Вывод системы уравнений в общем виде
    print("\n2. ВЫВОД СИСТЕМЫ УРАВНЕНИЙ В ОБЩЕМ ВИДЕ")
    print("-" * 80)

    print("\nФункция суммарной ошибки:")
    print("F(A₀, A₁) = Σ(Yᵢ - A₀ - A₁·Xᵢ)²")

    print("\nУсловия минимума:")
    print("∂F/∂A₀ = -2 Σ(Yᵢ - A₀ - A₁·Xᵢ) = 0")
    print("∂F/∂A₁ = -2 Σ[Xᵢ·(Yᵢ - A₀ - A₁·Xᵢ)] = 0")

    print("\nПосле деления на -2:")
    print("Σ(Yᵢ - A₀ - A₁·Xᵢ) = 0")
    print("Σ[Xᵢ·(Yᵢ - A₀ - A₁·Xᵢ)] = 0")

    print("\nРаскрываем суммы:")
    print("ΣYᵢ - n·A₀ - A₁·ΣXᵢ = 0")
    print("ΣXᵢYᵢ - A₀·ΣXᵢ - A₁·ΣXᵢ² = 0")

    print("\nПереносим свободные члены вправо:")
    print("n·A₀ + ΣXᵢ·A₁ = ΣYᵢ")
    print("ΣXᵢ·A₀ + ΣXᵢ²·A₁ = ΣXᵢYᵢ")

    print("\nСистема уравнений в общем виде:")
    print("⎧ n·A₀ + ΣX·A₁ = ΣY")
    print("⎩ ΣX·A₀ + ΣX²·A₁ = ΣXY")

    # 3. Решение системы в общем виде методом Крамера
    print("\n3. РЕШЕНИЕ СИСТЕМЫ В ОБЩЕМ ВИДЕ (МЕТОД КРАМЕРА)")
    print("-" * 80)

    print("\nМатричная форма системы:")
    print("⎡ n     ΣX ⎤ ⎡ A₀ ⎤   ⎡ ΣY ⎤")
    print("⎣ ΣX    ΣX² ⎦ ⎣ A₁ ⎦ = ⎣ ΣXY ⎦")

    print("\nГлавный определитель:")
    print("Δ = det ⎡ n     ΣX ⎤ = n·ΣX² - (ΣX)²")
    print("        ⎣ ΣX    ΣX² ⎦")

    print("\nОпределитель для A₀:")
    print("Δ₀ = det ⎡ ΣY     ΣX ⎤ = ΣY·ΣX² - ΣX·ΣXY")
    print("          ⎣ ΣXY    ΣX² ⎦")

    print("\nОпределитель для A₁:")
    print("Δ₁ = det ⎡ n     ΣY ⎤ = n·ΣXY - ΣX·ΣY")
    print("          ⎣ ΣX    ΣXY ⎦")

    print("\nФормулы для коэффициентов:")
    print("A₀ = Δ₀/Δ = (ΣY·ΣX² - ΣX·ΣXY) / (n·ΣX² - (ΣX)²)")
    print("A₁ = Δ₁/Δ = (n·ΣXY - ΣX·ΣY) / (n·ΣX² - (ΣX)²)")

    # 4. Таблица расчетов
    print("\n4. ТАБЛИЦА РАСЧЕТОВ")
    print("-" * 80)
    print(" i |   Xᵢ   |   Yᵢ   |   Xᵢ²   |   Xᵢ·Yᵢ   ")
    print("-" * 45)

    sum_X, sum_Y, sum_X2, sum_XY = 0, 0, 0, 0

    for i in range(n):
        xi = X[i]
        yi = Y[i]
        xi2 = xi ** 2
        xiyi = xi * yi

        sum_X += xi
        sum_Y += yi
        sum_X2 += xi2
        sum_XY += xiyi

        print(f"{i + 1:2d} | {xi:6.1f} | {yi:6.1f} | {xi2:7.1f} | {xiyi:8.1f}")

    print("-" * 45)
    print(f" Σ | {sum_X:6.1f} | {sum_Y:6.1f} | {sum_X2:7.1f} | {sum_XY:8.1f}")

    # 5. Подстановка в формулы
    print("\n5. ПОДСТАНОВКА В ФОРМУЛЫ И РАСЧЕТ КОЭФФИЦИЕНТОВ")
    print("-" * 80)

    print(f"\nЗначения сумм из таблицы:")
    print(f"ΣX = {sum_X}")
    print(f"ΣY = {sum_Y}")
    print(f"ΣX² = {sum_X2}")
    print(f"ΣXY = {sum_XY}")
    print(f"n = {n}")

    print(f"\nВычисляем определители:")

    # Вычисляем определители
    det = n * sum_X2 - sum_X ** 2
    det_A0 = sum_Y * sum_X2 - sum_X * sum_XY
    det_A1 = n * sum_XY - sum_X * sum_Y

    print(f"Δ = n·ΣX² - (ΣX)² = {n}·{sum_X2} - ({sum_X})²")
    print(f"  = {n * sum_X2} - {sum_X ** 2} = {det}")

    print(f"\nΔ₀ = ΣY·ΣX² - ΣX·ΣXY = {sum_Y}·{sum_X2} - {sum_X}·{sum_XY}")
    print(f"   = {sum_Y * sum_X2} - {sum_X * sum_XY} = {det_A0}")

    print(f"\nΔ₁ = n·ΣXY - ΣX·ΣY = {n}·{sum_XY} - {sum_X}·{sum_Y}")
    print(f"   = {n * sum_XY} - {sum_X * sum_Y} = {det_A1}")

    # Вычисляем коэффициенты
    A0 = det_A0 / det
    A1 = det_A1 / det

    print(f"\nВычисляем коэффициенты:")
    print(f"A₀ = Δ₀/Δ = {det_A0} / {det} = {A0:.6f}")
    print(f"A₁ = Δ₁/Δ = {det_A1} / {det} = {A1:.6f}")

    print(f"\nУравнение линейной регрессии:")
    print(f"Y = {A1:.6f}·X + {A0:.6f}")

    # 6. Расчет ошибок и стандартного отклонения
    print("\n6. РАСЧЕТ ОШИБОК И СТАНДАРТНОГО ОТКЛОНЕНИЯ")
    print("-" * 80)

    Y_theor = A1 * X + A0
    E = Y - Y_theor
    E2 = E ** 2

    print("\nТаблица расчетов ошибок:")
    print(" i |   Xᵢ   |   Yᵢ   |  Yᵢтеор  |   Eᵢ = Yᵢ-Yᵢтеор   |   Eᵢ²   ")
    print("-" * 70)

    for i in range(n):
        print(f"{i + 1:2d} | {X[i]:6.1f} | {Y[i]:6.1f} | {Y_theor[i]:8.4f} | {E[i]:18.6f} | {E2[i]:9.6f}")

    print("-" * 70)
    sum_E = np.sum(E)
    sum_E2 = np.sum(E2)
    print(f" Σ | {' ':6} | {' ':6} | {' ':8} | {sum_E:18.6f} | {sum_E2:9.6f}")

    print(f"\nСуммарная ошибка F = ΣEᵢ² = {sum_E2:.6f}")

    # Расчет σ
    sigma = np.sqrt(sum_E2 / n)
    print(f"\nСтандартное отклонение:")
    print(f"σ = √(F/n) = √({sum_E2:.6f}/{n}) = √{sum_E2 / n:.6f} = {sigma:.6f}")

    # 7. Расчет ширины полосы S
    print("\n7. РАСЧЕТ ШИРИНЫ ПОЛОСЫ S")
    print("-" * 80)

    # Угол наклона линии
    angle_rad = np.arctan(A1)
    angle_deg = np.degrees(angle_rad)
    beta = 90 - angle_deg
    beta_rad = np.radians(beta)
    sin_beta = np.sin(beta_rad)

    print(f"Расчет углов:")
    print(f"α = arctan(A₁) = arctan({A1:.6f}) = {angle_deg:.2f}°")
    print(f"β = 90° - α = 90° - {angle_deg:.2f}° = {beta:.2f}°")
    print(f"sin(β) = sin({beta:.2f}°) = {sin_beta:.6f}")

    # Расчет S
    S = sigma / sin_beta
    print(f"\nШирина полосы S:")
    print(f"S = σ/sin(β) = {sigma:.6f}/{sin_beta:.6f} = {S:.6f}")

    # 8. Определение доверительных границ
    print("\n8. ОПРЕДЕЛЕНИЕ ДОВЕРИТЕЛЬНЫХ ГРАНИЦ")
    print("-" * 80)

    # Полосы как в лекции: Yтеор - S и Yтеор + S
    Y_upper_S = Y_theor + S
    Y_lower_S = Y_theor - S

    # И также полоса ±2S для дополнительной проверки
    Y_upper_2S = Y_theor + 2 * S
    Y_lower_2S = Y_theor - 2 * S

    print("\nДоверительные границы для каждой точки (полоса ±S):")
    print(" i |   Yᵢ   |  Yтеор  | Yтеор-S | Yтеор+S | В полосе?")
    print("-" * 65)

    points_in_S = 0
    for i in range(n):
        in_S = Y_lower_S[i] <= Y[i] <= Y_upper_S[i]
        if in_S:
            points_in_S += 1

        symbol = "✓" if in_S else "✗"
        print(f"{i + 1:2d} | {Y[i]:6.1f} | {Y_theor[i]:7.3f} | {Y_lower_S[i]:7.3f} | {Y_upper_S[i]:7.3f} |   {symbol}")

    points_in_2S = sum((Y >= Y_lower_2S) & (Y <= Y_upper_2S))

    # 9. Проверка гипотезы
    print("\n9. ПРОВЕРКА ГИПОТЕЗЫ")
    print("-" * 80)

    percentage_S = (points_in_S / n) * 100
    percentage_2S = (points_in_2S / n) * 100

    print(f"Точек в полосе Yтеор ± S: {points_in_S} из {n} = {percentage_S:.2f}%")
    print(f"Точек в полосе Yтеор ± 2S: {points_in_2S} из {n} = {percentage_2S:.2f}%")

    print(f"\nКритерии принятия гипотезы:")
    print("- Если ≥68.26% точек в полосе Yтеор ± S → гипотеза принимается")
    print("- Если ≥95.44% точек в полосе Yтеор ± 2S → дополнительная уверенность")

    print(f"\nРезультат:")
    if percentage_S >= 68.26:
        print(f"✓ {percentage_S:.2f}% ≥ 68.26% → ГИПОТЕЗА ПРИНЯТА")
    else:
        print(f"✗ {percentage_S:.2f}% < 68.26% → гипотеза отклонена")

    if percentage_S >= 68.26:
        if percentage_2S >= 95.44:
            print(f"✓ {percentage_2S:.2f}% ≥ 95.44% → высокая уверенность в результате")
        else:
            print(f"→ умеренная уверенность в результате")

    # 10. График
    print("\n10. ГРАФИЧЕСКОЕ ПРЕДСТАВЛЕНИЕ")
    print("-" * 80)

    plt.figure(figsize=(12, 8))

    # Подготовка данных для графиков
    x_line = np.linspace(min(X) - 1, max(X) + 1, 100)
    y_line = A1 * x_line + A0
    y_upper_S_line = A1 * x_line + A0 + S
    y_lower_S_line = A1 * x_line + A0 - S
    y_upper_2S_line = A1 * x_line + A0 + 2 * S
    y_lower_2S_line = A1 * x_line + A0 - 2 * S

    # Полоса ±2S (светлая)
    plt.fill_between(x_line, y_lower_2S_line, y_upper_2S_line,
                     alpha=0.1, color='yellow', label='Полоса Yтеор ± 2S')

    # Полоса ±S (темнее)
    plt.fill_between(x_line, y_lower_S_line, y_upper_S_line,
                     alpha=0.3, color='lightgreen', label=f'Полоса Yтеор ± S (S={S:.3f})')

    # Регрессионная прямая
    plt.plot(x_line, y_line, 'r-', linewidth=3, label=f'Y = {A1:.3f}X + {A0:.3f}')

    # Экспериментальные точки
    plt.scatter(X, Y, color='blue', s=100, zorder=5, label='Экспериментальные точки')

    # Дополнительные линии границ
    plt.plot(x_line, y_upper_S_line, 'g--', linewidth=1, alpha=0.7, label='Yтеор + S')
    plt.plot(x_line, y_lower_S_line, 'g--', linewidth=1, alpha=0.7, label='Yтеор - S')

    # Настройки графика
    plt.xlabel('X (вход)', fontsize=12)
    plt.ylabel('Y (выход)', fontsize=12)
    plt.title('Линейная регрессия с доверительными полосами ±S и ±2S', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left')

    # Информация на графике
    info_text = f'Y = {A1:.3f}X + {A0:.3f}\n'
    info_text += f'σ = {sigma:.3f}\n'
    info_text += f'S = {S:.3f}\n'
    info_text += f'Точек в ±S: {points_in_S}/{n} ({percentage_S:.1f}%)\n'
    info_text += f'Точек в ±2S: {points_in_2S}/{n} ({percentage_2S:.1f}%)'

    plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    # Подписи точек
    for i, (x, y) in enumerate(zip(X, Y)):
        offset_x = 0.2 if i % 2 == 0 else -0.2
        plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points",
                     xytext=(offset_x * 15, 10), ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()

    # 11. Итоговый вывод
    print("\n" + "=" * 80)
    print("ИТОГОВЫЙ ВЫВОД")
    print("=" * 80)

    print(f"\n1. Уравнение линейной регрессии:")
    print(f"   Y = {A1:.4f}·X + {A0:.4f}")

    print(f"\n2. Результаты расчета:")
    print(f"   A₀ = {A0:.4f}")
    print(f"   A₁ = {A1:.4f}")
    print(f"   F = ΣE² = {sum_E2:.4f}")
    print(f"   σ = √(F/n) = {sigma:.4f}")
    print(f"   S = σ/sin(β) = {S:.4f}")

    print(f"\n3. Проверка гипотезы о линейности:")
    print(f"   Точек в полосе Yтеор ± S: {points_in_S}/{n} ({percentage_S:.2f}%)")

    if percentage_S >= 68.26:
        print(f"   ✓ Гипотеза принята (линейная модель адекватна)")
        print(f"   ✓ Точек в полосе Yтеор ± 2S: {points_in_2S}/{n} ({percentage_2S:.2f}%)")
        if percentage_2S >= 95.44:
            print(f"   ✓ Высокая уверенность в модели")
    else:
        print(f"   ✗ Гипотеза отклонена (нужна другая модель)")

    return {
        'A0': A0, 'A1': A1, 'sigma': sigma, 'S': S,
        'points_in_S': points_in_S, 'points_in_2S': points_in_2S,
        'percentage_S': percentage_S, 'percentage_2S': percentage_2S
    }


# Запуск анализа
if __name__ == "__main__":
    results = linear_regression_analysis()

    print("\n" + "=" * 80)
    print("ПРИМЕР ПРОГНОЗИРОВАНИЯ")
    print("=" * 80)

    print(f"\nИспользуем модель для прогноза:")
    print(f"Модель: Y = {results['A1']:.4f}·X + {results['A0']:.4f}")

    print("\nПрогноз с доверительными интервалами:")
    print(" X  |  Yпрогноз  |  Доверительный интервал (±S)")
    print("-" * 55)

    for x in [0, 5, 11, 15, 20]:
        y_pred = results['A1'] * x + results['A0']
        y_lower = y_pred - results['S']
        y_upper = y_pred + results['S']
        print(f"{x:3.0f} | {y_pred:10.4f} | [{y_lower:7.4f}, {y_upper:7.4f}]")